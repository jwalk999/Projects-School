"""
Program: Project 1.py
Author: Jonathan W
Date: 8/19/2026
Purpose: Get user's first name, last name, and birth year and print all

"""
#get the user's first name, last name, and birth year and input them as variables
firstname = input("Enter your first name: ")
lastname  = input("Enter your last name: ")
birthyear = input("Enter your birth year: ")

#display the user's first name, last name, and birth year as plain text
print(firstname)
print(lastname)
print(birthyear)

#tell the user who they are
greeting = f"You are {firstname} {lastname}, born in {birthyear}."
print(greeting)
