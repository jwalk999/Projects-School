"""
Program: Project 3c.py
Author: Jonathan Walker
Date: 8/26/2026
Purpose: Estimate the cost of fuel for a road trip

"""

# ===== INPUTS =====
# get the distance of the trip in miles
miles = input("How many miles will you be driving? ")
# get car's fuel efficiency in mpg
mpg = input("What is your car's fuel efficiency? (mpg) ")
# get current fuel price per gallon in dollars
price = input("How much is 1 gallon of gas? ($USD)")

# ===== CALCULATION =====
# calculate the gallons needed for the trip
total_gallons = float(miles) / float(mpg)
# calculate total cost of the trip
total_cost = float(total_gallons) * float(price)

# ===== OUTPUTS =====
# tell user how many gallons the trip will need
print("Gallons needed:", float(total_gallons))
# tell user how much the trip will cost in gas
print("Total cost:", float(total_cost))
