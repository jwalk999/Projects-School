"""
Program: Project 2.py
Author: Jonathan W
Date: 8/24/2026
Purpose: Get user's age then print it

"""

#Get user's age from a variable called age
age = int(input("Enter your age:"))


# age_message = "You are " + (age) + "years old."
# you cannot concatenate an integer into a string

age_message = "You are " + str(age) + " years old."
print(age_message)

