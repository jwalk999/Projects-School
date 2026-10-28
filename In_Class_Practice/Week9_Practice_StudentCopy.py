"""
Week 9 Extra Practice: Lists, Tuples, and Dictionaries
CIS 3680
Personal Budget Analyzer, ungraded, no submission, nothing here is graded or quizzed.
Fill in the TODOs yourself before checking your work against the Reference Sheet.
"""


def practice_1_lists():
    print("=== Practice 1: Lists, Expanding the Budget ===")

    weekly_expenses = [45.00, 120.50, 32.75, 89.00, 15.25]

    # TODO: add two more expenses to the list using .append()
    weekly_expenses.append(60.00)
    weekly_expenses.append(22.50)

    # TODO: compute total_spent and average_spent from the list
    total_spent = sum(weekly_expenses)
    average_spent = sum(weekly_expenses) / len(weekly_expenses)
    print(f"Total: ${total_spent:.2f}")
    print(f"Average: ${average_spent:.2f}")

    # TODO: sort the list from largest to smallest
    weekly_expenses.sort(reverse=False)
    print(f"Sorted List: {weekly_expenses}")
    

    # TODO: find the index of the largest expense in the sorted list
    largest_index = weekly_expenses.index(max(weekly_expenses))
    print(f"Largest Index: {largest_index}")
    smallest_index = weekly_expenses.index(min(weekly_expenses))
    print(f"Smallest Index: {smallest_index}\n \n")


def practice_2_tuples():
    print("=== Practice 2: Tuples, A Single Expense Record ===")

    expense_records = [
        ("Groceries", 350.00, "Essential"),
        ("Streaming", 15.99, "Discretionary"),
        ("Rent", 900.00, "Essential"),
    ]

    # TODO: loop through expense_records, unpacking each tuple into
    # name, amount, category_type, and print a formatted line for each
    print("Records (not unpacked yet):", expense_records)
    print()

    print("Records (unpacked)")
    for name, amount, category_type in expense_records:
        print(f"{name}: $ {amount:.2f}: {category_type}")
    print()

    # TODO: try changing a value inside one of these tuples, for example
    # expense_records[0][1] = 400.00
    # Run it and read the error. What is Python telling you, and why?

    


def practice_3_dictionaries():
    print("=== Practice 3: Dictionaries, Expanding the Categories ===")

    budget = {
        "income": 2500.00,
        "rent": 900.00,
        "groceries": 350.00,
        "utilities": 150.00,
    }

    # TODO: add a new "savings" category to the dictionary
    print("Current budget:", budget)
    budget["savings"] = 200.00

    # TODO: use .get() to check for an "entertainment" category that
    # isn't in the dictionary, with a default of 0.00
    entertainment = budget.get("entertainment", 0.00)
    print(entertainment)


    # TODO: loop over every category except "income", and for each one
    # print the category name, its amount, and what percent of income
    # it represents
    for category, amount in budget.items():
        if category != "income":
            percent = (amount / budget["income"]) * 100
            print(f"{category.title()}: ${amount:.2f} - {percent:.1f}% of income")
    print()

    print("Add savings:", budget)
    print()


def practice_4_strings():
    print("=== Practice 4: Strings, Parsing Several Raw Lines at Once ===\n")

    raw_lines = [
        "  Groceries, 350.00, Essential  ",
        "Streaming,15.99,Discretionary",
        " Rent , 900.00 , Essential ",
    ]

    # TODO: build a list named parsed. For each raw line, strip it,
    # split it on commas, strip each piece, convert the amount to
    # float, and append a (name, amount, category_type) tuple to parsed
    print("Raw lines (not parsed yet):", raw_lines)
    print()


    for item in raw_lines:
        cleaned = item.strip()
        parts = cleaned.split(",")
        name = parts[0].strip()
        amount = float(parts[1].strip())
        category = parts[2].strip()
        parsed = (f"{name.title()}: ${amount:.2f} -- {category}")
        print(parsed)

    # TODO: build a dictionary named lookup that maps each name to its
    # amount, using the records in parsed
    lookup = {}

    for item in raw_lines:
        cleaned = item.strip()
        parts = cleaned.split(",")
        name = parts[0].strip()
        amount = float(parts[1].strip())
        lookup[name] = amount
    print(lookup)




if __name__ == "__main__":
    practice_1_lists()
    practice_2_tuples()
    practice_3_dictionaries()
    practice_4_strings()
