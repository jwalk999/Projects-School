"""
Program: bmi.py
Author: Jonathan Walker
Date: 8/24/2026
Purpose: Calculate the user's Body Mass Index (BMI)
        The program accepts weight in pounds and height in inches,
        converts to metric units, and outputs the BMI calculation.
"""
# Conversion constants
# convert the input into metric to calculate
LBS_TO_KG = 0.453592 # conversion factor: pounds to kilograms
INCHES_TO_METERS = 0.0254 # conversion factor: inches to meters

# ===== INPUT SECTION =====
# Get user inputs to define weight and height
weight_lbs = int(input("Enter your weight (pounds): "))
height_in = int(input("Enter your height (inches): "))

# ===== CONVERSION SECTION =====
# Convert imperial units to metric units
weight_kg = weight_lbs * LBS_TO_KG
height_m = height_in * INCHES_TO_METERS

# ===== CALCULATION SECTION =====
# Calculate BMI using the formula: BMI = weight (kg) / (height (m))^2
bmi = weight_kg / height_m ** 2

# ===== OUTPUT SECTION =====
bmi_output = f"Your BMI is  {bmi}"
print(bmi_output)

# remove huge decimal
#bmi_output_integer = f"Your BMI is {int(bmi)}"
#print(bmi_output_integer)