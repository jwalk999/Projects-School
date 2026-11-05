"""In-Class Practice 12: Classes and the Budget Analyzer (Monday).

CIS 3680, Prof. Taylor
Ungraded, no submission. Follow along in class and fill in each TODO.
"""


class BudgetAnalyzer:
    """Tracks one household's income and expenses."""

    def __init__(self, income: float):
        self.income = income
        self.expenses: dict[str, float] = {}

    def add_expense(self, category: str, amount: float) -> None:
        """Add an expense to the given category."""
        self.expenses[category] = self.expenses.get(category, 0) + amount

    def total_expenses(self) -> float:
        """Return the sum of all recorded expenses."""
        return sum(self.expenses.values())

    def remaining_balance(self) -> float:
        """Return income minus total expenses."""
        return self.income - self.total_expenses()

    def average_expense(self) -> float:
        """Return the average expense amount across all categories."""
        if not self.expenses:
            return 0.0
        return self.total_expenses() / len(self.expenses)

    def summary(self) -> str:
        """Return a formatted summary of this tracker's state."""
        return (
            f"Income: ${self.income:.2f}\n"
            f"Expenses: ${self.total_expenses():.2f}\n"
            f"Remaining Balance: ${self.remaining_balance():.2f}\n"
            f"Average Expense: ${self.average_expense():.2f}\n"
        )


class Household:
    """Pairs a household name with its BudgetAnalyzer."""

    def __init__(self, name: str, tracker: BudgetAnalyzer):
        self.name = name
        self.tracker = tracker

    def report(self) -> str:
        """Return a one-line report combining the name and remaining balance."""
        return f"{self.name}: ${self.tracker.remaining_balance():.2f} remaining"


def main() -> None:
    # Two independent households built from the same blueprint.
    smith_tracker = BudgetAnalyzer(3000.00)
    smith_tracker.add_expense("Groceries", 150.00)
    smith_tracker.add_expense("Rent", 1200.00)

    nguyen_tracker = BudgetAnalyzer(4200.00)
    nguyen_tracker.add_expense("Groceries", 220.00)
    nguyen_tracker.add_expense("Rent", 1500.00)
    nguyen_tracker.add_expense("Utilities", 180.00)

    print("--- Smith household ---")
    print(smith_tracker.summary())
    print()
    print("--- Nguyen household ---")
    print(nguyen_tracker.summary())
    print()

    smith = Household("Smith Family", smith_tracker)
    nguyen = Household("Nguyen Family", nguyen_tracker)
    print(smith.report())
    print(nguyen.report())

    walker_tracker = BudgetAnalyzer(2500)
    walker_tracker.add_expense("Rent", 825.00)
    walker_tracker.add_expense("Utilities", 100.00)
    walker_tracker.add_expense("Groceries", 200.00)
    walker_tracker.add_expense("Car Payment", 275.00)
    walker_tracker.add_expense("Gas", 100)
    print()
    print("----- Walker -----")
    print(walker_tracker.summary())
    walker = Household("Walker", walker_tracker)
    print(walker.report())


if __name__ == "__main__":
    main()
