"""
Week 11 In-Class Practice: Personal Budget Analyzer
CIS 3680, Prof. Taylor

Ungraded, no submission. Extends the budget analyzer with:
  - try/except around expense amount entry (Monday)
  - regex validation of a category code, format BUD-### (Wednesday)
"""

import re
import matplotlib.pyplot as plt

CATEGORY_CODE_PATTERN = r"^BUD-\d{3}$"


def get_income() -> float:
    """Prompt for and return the user's income as a float."""
    income_input = input("Enter your income for this month: ")

    try:
        income = float(income_input)
    except ValueError:
        print("Invalid entry, default income = 0.")
        income = 0.0

    return income


def add_expense(expenses: dict) -> None:
    """
    Prompt for a category code and amount, validate both, and add the
    expense to the expenses dict. Does nothing if either value is invalid.
    """
    category_code = input("Enter the category code (format BUD-###): ")

    if not re.fullmatch(CATEGORY_CODE_PATTERN, category_code):
        print(f"'{category_code}' does not match the expected format: BUD-###")
        return

    amount_input = input(f"Enter the amount for {category_code}: ")

    try:
        amount = float(amount_input)
        if amount < 0:
            raise ValueError("Expense cannot be negative.")
    except ValueError as e:
        print(f"Invalid entry: {e}")
        return

    expenses[category_code] = expenses.get(category_code, 0) + amount
    print(f"Added ${amount:.2f} to {category_code}.")


def summarize(income: float, expenses: dict) -> None:
    """Print a summary of income, expenses, remaining budget, and savings rate."""
    total_expenses = sum(expenses.values())
    remaining = income - total_expenses
    savings_rate = (remaining / income * 100) if income > 0 else 0.0

    print()
    print(f"Income: ${income:.2f}")
    print(f"Total expenses: ${total_expenses:.2f}")
    print(f"Remaining: ${remaining:.2f}")
    print(f"Savings rate: {savings_rate:.1f}%")


def show_chart(expenses: dict) -> None:
    """Display a bar chart of expenses by category code."""
    if not expenses:
        print("No expenses to chart yet.")
        return
    plt.bar(expenses.keys(), expenses.values())
    plt.title("Expenses by Category")
    plt.xlabel("Category Code")
    plt.ylabel("Amount ($)")
    plt.savefig("budget_chart.png")
    print("Chart saved to budget_chart.png")


def main() -> None:
    expenses = {}
    income = get_income()

    while True:
        choice = input("\n(a)dd expense, (s)ummary, (c)hart, (q)uit: ").strip().lower()
        if choice == "a":
            add_expense(expenses)
        elif choice == "s":
            summarize(income, expenses)
        elif choice == "c":
            show_chart(expenses)
        elif choice == "q":
            break
        else:
            print("Not a recognized option.")


if __name__ == "__main__":
    main()
