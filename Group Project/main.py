"""
File Name: main.py
Authors: Jonathan Walker, Briana Campbell, Isaiah McSwain
Date: 13 Nov 2026

Scope: Bridge the .py files, acting as a launcher.
"""

import tkinter as tk

from entities import Client
from main_gui import DeveloperDashboard


def main() -> None:
    """Creates sample data and starts the dashboard."""
    client = Client(
        "Example Realty Co.",
        "contact@example.com",
        "828-555-0100",
        ["Contact form", "Property listings", "Image gallery"],
    )
    root = tk.Tk()
    DeveloperDashboard(root, client)
    root.mainloop()


if __name__ == "__main__":
    main()
