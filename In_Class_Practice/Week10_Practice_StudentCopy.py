"""
Week 10 Extra Practice: JSON
CIS 3680
Personal Budget Analyzer, ungraded, no submission, nothing here is graded or quizzed.
Fill in the TODOs yourself before checking your work against the Reference Sheet.
"""

import json


def practice_1_reading():
    print("=== Practice 1: Reading a JSON Budget ===")

    budget = {
        "income": 2500.00,
        "rent": 900.00,
        "groceries": 350.00,
        "utilities": 150.00,
    }
    with open("budget.json", "w") as f:
        json.dump(budget, f, indent=2)

    # TODO: open "budget.json" for reading and load it with json.load(),
    # replacing the budget variable with what comes back

    with open("budget.json", "r") as f:
        budget = json.load(f)


    # TODO: loop over the loaded budget's categories and amounts,
    # printing each one formatted like Week 9's budget loop

    for category, amount in budget.items():
        print(f"{category.title()}: ${amount:.2f}")
    print()
    print("Budget written to file, not loaded back yet:", budget)
    print()
    return budget


def practice_2_writing(budget):
    print("=== Practice 2: Modifying and Writing It Back ===")

    # TODO: add a new "savings" category worth 200.00 to budget
    budget["savings"] = 200.00

    # TODO: write budget to a new file named "budget_updated.json"
    # using json.dump(), with indent=2 for readability
    with open("budget_updated.json", "w") as f:
        json.dump(budget, f, indent=2)
    with open("budget_updated.json", "r") as f:
        print(f.read())
    print()

    print("Current budget:", budget)
    print()


def practice_3_csv_to_json():
    print("=== Practice 3: From CSV Parsing to JSON ===")

    raw_lines = [
        "  Groceries, 350.00, Essential  ",
        "Streaming,15.99,Discretionary",
        " Rent , 900.00 , Essential ",
    ]

    # TODO: build a list named parsed. For each raw line, strip it,
    # split it on commas, strip each piece, convert the amount to
    # float, and append a dictionary with keys "name", "amount", and
    # "type" to parsed
    parsed = []
    for item in raw_lines:
        parts = item.strip().split(",")
        name = parts[0].strip()
        amount = float(parts[1].strip())
        category_type = parts[2].strip()
        parsed.append({"name" : name, "amount": amount, "type": category_type})
    

    # TODO: write parsed to a new file named "expenses.json" using
    # json.dump(), with indent=2

    with open("expenses.json", "w") as f:
        json.dump(parsed, f, indent=2)

    with open("expenses.json", "r") as f:
        print(f.read())

    print("Raw lines (not parsed yet):", raw_lines)
    print()


def practice_4_nested():
    print("=== Practice 4: A Nested JSON Structure ===")

    monthly_budget = {
        "month": "October",
        "income": 2500.00,
        "expenses": {
            "rent": 900.00,
            "groceries": 350.00,
        },
    }
    with open("monthly_budget.json", "w") as f:
        json.dump(monthly_budget, f, indent=2)

    # TODO: open "monthly_budget.json" and load it into a variable
    # named data
    with open("monthly_budget.json", "r") as f:
        data = json.load(f)

    # TODO: print the month, then compute and print the total of
    # data["expenses"], then loop over data["expenses"] and print
    # each category and amount

    print("File written, not loaded back yet.")
    print()


if __name__ == "__main__":
    budget = practice_1_reading()
    practice_2_writing(budget)
    practice_3_csv_to_json()
    practice_4_nested()
