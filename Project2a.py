"""
Program: Project 2.py
Author: Jonathan W
Date: 8/24/2026
Purpose: Get user's name and age then greet them

"""
# get the user's first name, last name, and age, store them as variables
first_name = input("Enter your first name: ")
last_name = input ("Enter your last name: ")
# 'age' will be stored as an integer rather than a string
age = int(input("Enter your age: "))

greeting = f"Hello,   {first_name}  {last_name}  . You are   {str(age)}   years old!"

print(greeting)
