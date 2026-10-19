"""
CIS 3680 - Week 7: Functions, Parameters, Return Values
Personal Budget Analyzer - In-Class Starter File
Name:

Bring this file to class both days. Type along during the demo parts.
Fill in every TODO during Guided Practice. This file is not graded,
it's practice before Lab 5.
"""

# ============================================================
# MONDAY: FUNCTION ANATOMY, TYPE HINTS, RETURN VS. PRINT
# ============================================================

# ----- Part 0: The old way (no function) -----

income = 3600.00
rent = 1200.00
utilities = 180.00
groceries = 420.00
subscriptions = 45.00

total_expenses = rent + utilities + groceries + subscriptions
savings = income - total_expenses
print(f"Savings (no function): {savings}")


# ----- Part 1: Anatomy of a function, with type hints -----

def calculate_total_expenses(rent: float, utilities: float, groceries: float, subscriptions: float) -> float:
    """Add up a household's monthly expense categories.

    Args:
        rent: Monthly rent or mortgage payment.
        utilities: Monthly utilities cost.
        groceries: Monthly groceries cost.
        subscriptions: Monthly subscription costs.

    Returns:
        The sum of all four expense categories.
    """
    return rent + utilities + groceries + subscriptions

# return the sum of all 4 parameters
total = calculate_total_expenses(rent, utilities, groceries, subscriptions)
print(f"Total Expenses (function): {total}")

# ----- Part 2: Return vs. print, watch it happen -----

def calculate_total_expenses_PRINT_VERSION(rent: float, utilities: float, groceries: float, subscriptions: float) -> None:
    """Same math, printed instead of returned. For comparison only."""
    print(rent + utilities + groceries + subscriptions)


result = calculate_total_expenses_PRINT_VERSION(rent, utilities, groceries, subscriptions)
print(f"What did we get back? {result}")


# ============================================================
# GUIDED PRACTICE (Monday, ~30 min, on your own)
# ============================================================
# Write ONE new function below. Pick one idea, or come up with your own:
#
#   calculate_emergency_fund_target(total_expenses: float) -> float
#       Returns total_expenses * 6 (a common rule of thumb: 6 months
#       of expenses saved up).
#
#   calculate_expense_percentage(category_amount: float, total_expenses: float) -> float
#       Returns what percent one expense category is of the total
#       (category_amount / total_expenses * 100).
#
#   calculate_annual_savings(monthly_savings: float) -> float
#       Returns monthly_savings * 12.
#
# Requirements: type hints on every parameter and the return value,
# a docstring with Args and Returns, and it must return a value,
# not print one. Call your function below it and print the result
# to check your work.

# TODO: your function here


# TODO: call your function here and print the result


# ============================================================
# WEDNESDAY: COMPOSITION, GUARD CLAUSES, LOCAL SCOPE
# ============================================================

# ----- Part 3: Guard clauses -----

INVALID_SAVINGS = -1.0

def calculate_savings(income: float, total_expenses: float) -> float:
    """Calculate how much of income is left after expenses.

    Args:
        income: Monthly income.
        total_expenses: Monthly expenses, from calculate_total_expenses().

    Returns:
        income minus total_expenses, or INVALID_SAVINGS if income
        is not a positive number.
    """
    # TODO: guard clause. If income is not positive, return
    # INVALID_SAVINGS here before doing any math.

    # TODO: return income minus total_expenses.
    pass


# ----- Part 4: Function composition -----

def calculate_savings_rate(income: float, total_expenses: float) -> float:
    """Calculate savings as a percentage of income.

    Args:
        income: Monthly income.
        total_expenses: Monthly expenses.

    Returns:
        Savings rate as a percentage, or INVALID_SAVINGS if income
        is not a positive number.
    """
    # TODO: call calculate_savings(income, total_expenses) and store
    # the result.

    # TODO: if that result equals INVALID_SAVINGS, return
    # INVALID_SAVINGS.

    # TODO: otherwise return (savings / income) * 100.
    pass


def display_budget_summary(income: float, total_expenses: float, savings: float, savings_rate: float) -> None:
    """Print the budget results. The only function in this file that prints."""
    print(f"Income: {income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Savings: {savings}")
    print(f"Savings Rate: {savings_rate:.1f}%")


total_expenses = calculate_total_expenses(rent, utilities, groceries, subscriptions)
savings = calculate_savings(income, total_expenses)
savings_rate = calculate_savings_rate(income, total_expenses)
display_budget_summary(income, total_expenses, savings, savings_rate)


# ----- Part 5: Local scope -----

def function_one() -> int:
    bmi_style_total = 100
    return bmi_style_total


def function_two() -> int:
    bmi_style_total = 999
    return bmi_style_total


print(f"function_one(): {function_one()}")
print(f"function_two(): {function_two()}")


# ============================================================
# GUIDED PRACTICE (Wednesday, ~20 min, on your own)
# ============================================================
# Go back to the function you wrote Monday. Add a guard clause to it,
# same pattern as calculate_savings above: check for a bad input
# first, and return a sentinel value before doing any math if the
# input doesn't make sense (for example, a negative amount).
#
# Pick a sentinel value and give it a named constant, same style as
# INVALID_SAVINGS above.

# TODO: your guard clause goes inside the function you wrote Monday,
# not here. Come back up and edit it directly.
