"""
File Name: ssn.py
Author: Jonathan W.
Date: 10/28/2026
Scope: Practicing regular expressions and error handling.
"""

import re

# Regex rules
SOCIAL_SECURITY_PATTERN = r"^\d{3}\d{2}\d{4}$"


def give_me_ur_munny():
    # Make sure entered text is only numbers
    checker = "1234567890"

    # Input and Error Handling
    # If not number -> ValueError
    stealer = input("Enter SSN or (q)uit: ").strip()
    if stealer == "q":
        return False

    try:
        replacer = stealer.replace("-", "")
        for x in replacer:
            if x not in checker:
                raise ValueError("That's not a number!")

    # I don't think this does anything since it is a string.
    except TypeError:
        print("Can we use int?")
        return

    # Match regex rules
    if not re.fullmatch(SOCIAL_SECURITY_PATTERN, replacer):
        print(f"Wrong Format!")

    else:
        print(f"I am has ur munny naow >:)")


def main():
    while True:
        give_me_ur_munny()


if __name__ == "__main__":
    main()
