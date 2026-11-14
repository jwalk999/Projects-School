"""Developer progress dashboard (GUI only).

File Name: main_gui.py
Authors: Jonathan Walker, Briana Campbell, Isaiah McSwain
Date: 9 Nov 2026

Scope:
    A GUI template any freelance developer can use to show clients the
    progress on their project. This file only builds and updates the
    window. It holds no program logic: loading JSON, comparing files,
    and fetching GitHub commits live in other modules, which hand their
    results to this dashboard to display.
"""

import tkinter as tk
from tkinter import ttk

import matplotlib

# Tell matplotlib to draw into tkinter. This must run before the
# backend import below, which is why that import isn't at the top.
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ---------------------------------------------------------------------------
# Mock data
# Stand-in for the output of the JSON diff module. Each change is a dict
# with "type" ("added", "changed", or "removed"), "description", and
# "date" (YYYY-MM-DD). Replace with real data once that module is ready.
# ---------------------------------------------------------------------------
MOCK_CHANGES = [
    {"type": "added", "description": "Contact form fields", "date": "2026-11-12"},
    {"type": "changed", "description": "Home page hero image", "date": "2026-11-11"},
    {"type": "removed", "description": "Old placeholder text", "date": "2026-11-10"},
]


class DeveloperDashboard:
    """Main dashboard window.

    The window is a stack of rows, top to bottom:
        header -> summary cards -> middle panels -> bottom panels -> dev tools

    Each row is a Frame. Rows are stacked with pack(); panels inside a row
    sit side by side using grid().

    Methods follow a "build once, update many times" pattern:
        build_* methods create widgets one time, at startup.
        draw_* / show_* methods refresh what those widgets display.
    """

    def __init__(self, root: tk.Tk, width: int = 1200, height: int = 800) -> None:
        """Sets up the main window and builds every section.

        Args:
            root: The main tkinter window.
            width: Starting window width in pixels.
            height: Starting window height in pixels.
        """
        self.root = root
        self.width = width
        self.height = height

        # False = developer view (dev tools shown), True = client view.
        self.client_view = False

        self.root.title("Dev Dashboard")
        self.root.geometry(f"{self.width}x{self.height}")

        self.build_layout()

    # -----------------------------------------------------------------------
    # Layout
    # -----------------------------------------------------------------------

    def build_layout(self) -> None:
        """Creates the row frames, builds each section, and loads starting data."""
        # pack() order = screen order, so these appear top to bottom.
        # fill="x": stretch sideways only, keep natural height.
        # fill="both", expand=True: also share any leftover window height.
        self.header_frame = tk.Frame(self.root, padx=10, pady=10)
        self.header_frame.pack(side="top", fill="x")

        self.cards_frame = tk.Frame(self.root, padx=10)
        self.cards_frame.pack(side="top", fill="x")

        self.middle_frame = tk.Frame(self.root, padx=10, pady=10)
        self.middle_frame.pack(side="top", fill="both", expand=True)

        self.bottom_frame = tk.Frame(self.root, padx=10, pady=10)
        self.bottom_frame.pack(side="top", fill="both", expand=True)

        # Hidden in client view (see toggle_view).
        self.dev_frame = tk.Frame(self.root, padx=10, pady=10)
        self.dev_frame.pack(side="top", fill="x")

        # Build each section. Panels must exist before anything placed
        # inside them, so build_middle_row comes before the pie and log.
        self.build_header()
        self.build_cards()
        self.build_middle_row()
        self.build_pie_graph()
        self.build_changes_log()
        self.build_bottom_row()
        self.build_dev_row()

        # Placeholder data until the data modules are connected.
        self.draw_pie(80)
        self.show_changes(MOCK_CHANGES)

    def make_panel(self, parent: tk.Frame, title: str, column: int) -> tk.LabelFrame:
        """Creates a titled, bordered panel in a row.

        Args:
            parent: The row frame the panel goes in.
            title: Text shown in the panel's border.
            column: Grid column within the row (0 = leftmost).

        Returns:
            The new panel, so widgets can be placed inside it.
        """
        panel = tk.LabelFrame(parent, text=title, padx=10, pady=10)
        # sticky="nsew" stretches the panel to all four edges of its cell.
        panel.grid(row=0, column=column, sticky="nsew", padx=5)
        return panel

    # -----------------------------------------------------------------------
    # Header
    # -----------------------------------------------------------------------

    def build_header(self) -> None:
        """Creates the project title, client and deadline info, and view toggle."""
        # Sub-frame so the three labels stack vertically on the left.
        self.info_frame = tk.Frame(self.header_frame)
        self.info_frame.pack(side="left")

        self.title_label = tk.Label(self.info_frame, text="Project Name",
                                    font=("Arial", 18, "bold"))
        self.title_label.pack(anchor="w")

        self.client_name = tk.Label(self.info_frame, text="Client: ",
                                    font=("Arial", 12))
        self.client_name.pack(anchor="w")

        self.deadline = tk.Label(self.info_frame, text="Deadline: ",
                                 font=("Arial", 12))
        self.deadline.pack(anchor="w")

        self.view_button = tk.Button(self.header_frame, text="Client view",
                                     command=self.toggle_view)
        self.view_button.pack(side="right")

    def toggle_view(self) -> None:
        """Switches between developer view and client view.

        Client view hides the dev tools row. The button text always names
        the view you would switch to.
        """
        self.client_view = not self.client_view  # Flip True <-> False

        if self.client_view:
            self.dev_frame.pack_forget()  # Hides the frame without destroying it
            self.view_button.config(text="Developer view")
        else:
            self.dev_frame.pack(side="top", fill="x")  # Re-packs at the bottom
            self.view_button.config(text="Client view")

    # -----------------------------------------------------------------------
    # Summary cards
    # -----------------------------------------------------------------------

    def build_cards(self) -> None:
        """Creates the row of four summary cards."""
        # Equal weights so the four cards share the width evenly.
        for column in range(4):
            self.cards_frame.columnconfigure(column, weight=1)

        # Each card's number label is saved so it can be updated later,
        # e.g. self.progress_card.config(text="48%").
        self.progress_card = self.make_card(0, "Overall progress")
        self.deadline_card = self.make_card(1, "Days to deadline")
        self.commits_card = self.make_card(2, "Commits this week")
        self.hours_card = self.make_card(3, "Hours logged")

    def make_card(self, column: int, label_text: str) -> tk.Label:
        """Creates one summary card: a small caption above a large value.

        Args:
            column: Grid column in the cards row (0-3).
            label_text: Caption shown at the top of the card.

        Returns:
            The value label, so its text can be updated later.
        """
        card = tk.Frame(self.cards_frame, padx=10, pady=10, relief="groove", bd=2)
        card.grid(row=0, column=column, sticky="nsew", padx=5)

        caption = tk.Label(card, text=label_text, font=("Arial", 12), padx=10, pady=10)
        caption.pack(anchor="w")

        value_label = tk.Label(card, text="--", font=("Arial", 16), padx=10, pady=10)
        value_label.pack(anchor="w")
        return value_label

    # -----------------------------------------------------------------------
    # Middle row: milestone progress and recent changes
    # -----------------------------------------------------------------------

    def build_middle_row(self) -> None:
        """Creates the milestone progress and recent changes panels."""
        # Equal column weights split the width 50/50.
        self.middle_frame.columnconfigure(0, weight=1)
        self.middle_frame.columnconfigure(1, weight=1)
        self.middle_frame.rowconfigure(0, weight=1)

        self.milestone_panel = self.make_panel(self.middle_frame, "Milestone Progress", 0)
        self.changes_panel = self.make_panel(self.middle_frame, "Recent Changes", 1)

    def build_pie_graph(self) -> None:
        """Creates the pie chart area. Drawing happens in draw_pie().

        Temporary home in the milestone panel until progress bars replace it.
        """
        # figsize is in inches; at the default 100 dpi, (2, 2.5) is ~200x250 px.
        self.figure = Figure(figsize=(2, 2.5))
        self.ax = self.figure.add_subplot(111)  # 1 row, 1 column, plot #1
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.milestone_panel)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def draw_pie(self, done: int) -> None:
        """Redraws the pie chart with a new completion percentage.

        Args:
            done: Percent of the project complete (0-100).
        """
        self.ax.clear()
        self.ax.pie([done, 100 - done], labels=["Done", "Remaining"], autopct="%1.0f%%")
        self.ax.set_title("Project Progress")
        self.canvas.draw()  # Required, or the window never shows the new chart

    def build_changes_log(self) -> None:
        """Creates the table that lists recent changes. Filled by show_changes()."""
        # Default ttk row height clips text on scaled displays, so raise it.
        style = ttk.Style()
        style.configure("Treeview", rowheight=28)

        columns = ("type", "description", "date")  # Internal column IDs
        self.changes_tree = ttk.Treeview(self.changes_panel, columns=columns,
                                         show="headings", height=8)  # height = rows

        # Text shown at the top of each column
        self.changes_tree.heading("type", text="Type")
        self.changes_tree.heading("description", text="Description")
        self.changes_tree.heading("date", text="Date")

        self.changes_tree.column("type", width=80, anchor="center")
        self.changes_tree.column("description", width=250)
        self.changes_tree.column("date", width=100, anchor="center")

        # Row colors, matched to each change's "type" tag in show_changes()
        self.changes_tree.tag_configure("added", foreground="green")
        self.changes_tree.tag_configure("changed", foreground="blue")
        self.changes_tree.tag_configure("removed", foreground="red")

        self.changes_tree.pack(fill="both", expand=True)

    def show_changes(self, changes: list[dict[str, str]]) -> None:
        """Clears the change log and fills it with new changes.

        Args:
            changes: Change records, each with "type", "description", and
                "date" keys. See MOCK_CHANGES for the expected format.
        """
        # Remove every existing row before adding the new ones.
        self.changes_tree.delete(*self.changes_tree.get_children())

        for change in changes:
            self.changes_tree.insert(
                "",     # Top level (no parent row)
                "end",  # Add to the bottom
                values=(change["type"], change["description"], change["date"]),
                tags=(change["type"],),  # Trailing comma makes this a tuple
            )

    # -----------------------------------------------------------------------
    # Bottom row: commit activity and upcoming milestones
    # -----------------------------------------------------------------------

    def build_bottom_row(self) -> None:
        """Creates the commit activity and upcoming milestones panels."""
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.rowconfigure(0, weight=1)

        self.commits_panel = self.make_panel(self.bottom_frame, "Recent Commit Activity", 0)
        self.upcoming_milestones_panel = self.make_panel(
            self.bottom_frame, "Upcoming Milestones", 1)

    # -----------------------------------------------------------------------
    # Developer tools (hidden in client view)
    # -----------------------------------------------------------------------

    def build_dev_row(self) -> None:
        """Creates the developer-only buttons.

        The buttons have no commands yet. They will call the data modules
        (JSON loading, GitHub sync) once those exist.
        """
        self.dev_tools_label = tk.Label(self.dev_frame,
                                        text="Developer tools (hidden in client view)",
                                        font=("Arial", 16, "bold"))
        self.dev_tools_label.pack(side="left")

        self.load_old_button = tk.Button(self.dev_frame, text="Load old JSON",
                                         padx=10, pady=10)
        self.load_new_button = tk.Button(self.dev_frame, text="Load new JSON",
                                         padx=10, pady=10)
        self.sync_github_button = tk.Button(self.dev_frame, text="Sync GitHub",
                                            padx=10, pady=10)
        self.notes_button = tk.Button(self.dev_frame, text="Note to Client",
                                      padx=10, pady=10)

        for button in (self.load_old_button, self.load_new_button,
                       self.sync_github_button, self.notes_button):
            button.pack(side="left", anchor="s")


def main() -> None:
    """Creates the window and starts the tkinter event loop."""
    root = tk.Tk()
    DeveloperDashboard(root)
    root.mainloop()  # Keeps the window open; code after this runs only on close


if __name__ == "__main__":
    main()
