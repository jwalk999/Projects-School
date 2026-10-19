"""
Program: Project 3b.py
Author: Jonathan Walker
Date: 8/26/2026
Purpose: Calculator that takes a birth year and outputs in 3 different units
        - regular years
        - dog years (x * 7)
        - Mars years (x / 1.88)
"""
# ===== INPUTS =====
# get the current year
current_year = int(input("What year is it now? "))
# get user's birth year
birth_year = int(input("Enter your birth year: "))

# ===== CALCULATOR =====
# calculate user's age in regular years
age_years = current_year - birth_year
# calculate user's age in dog years
# formula = regular years * 7
dog_years = age_years * 7  
# calculate user's age in Mars years
# formula = user's age / 1.88
mars_years = age_years / 1.88  #float

# ===== OUTPUT =====
# tell the user their age in regular years
print("You are " + str(age_years) + " years old.")
# tell the user their age in dog years
print("In dog years, that is", dog_years)
# tell the user their age in Mars years
print("In Mars years, that is", mars_years)