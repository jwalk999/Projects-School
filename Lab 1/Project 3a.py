"""
Program: Project 3a.py
Author: Jonathan Walker
Date: 8/26/2026
Purpose: Receive a user's personal info and generate a secret agent code
        - get first name, favorite color, and birth month as string
        - combine the first 3 letters of each and turn it into a user code

"""

# ===== INPUTS =====
# get user's first name
first_name = input("Please enter your name: ")
# get user's favorite color
user_color = input("Please enter your favorite color: ")
# get user's birth month as string
birth_month = input("Please enter your birth month as a word (March, etc.) :")

# ===== COMBINATION =====
# combine first 3 letters of each input into a secret agent code
agent_code = first_name[:3] + user_color[:3] + birth_month[:3]

# ===== OUTPUT =====
# tell the user their code
print("Your agent code is: ", agent_code)