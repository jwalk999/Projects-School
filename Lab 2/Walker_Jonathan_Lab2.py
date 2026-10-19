'''
Program: Walker_Jonathan_Lab2.py
Author: Jonathan Walker
Date: 9/2/2026
Purpose: Patient Body Metrics Calculator
        1. Prompt user for patient's weight in kilograms
        2. Prompt user for patient's height in meters
        3. Calculate body surface area using Mosteller formula
        4. Calculate Ponderal Index
        5. Print both results, clearly labeled, round to 2 decimal places
'''

#===== INPUTS =====
weight_kg = float(input("Enter the patient's weight in kg: "))
height_m = float(input("Enter the patient's height in meters: "))
# inputs are converted from string to float

#===== CALCULATIONS ====

'''
Body Surface Area: Mosteller formula
        BSA = sqrt(( height_cm * weight_kg ) / 3600 )

Ponderal Index
        PI = wight_kg / (height_m ** 3)

'''
# must convert from meters to centimeters
# python has no square root, so must use fractional exponent
bsa = ((height_m * 100 * weight_kg) / 3600 ) ** 0.5
# ** 0.5 = x to the power of 0.5
# ** = exponent
ponderal_index = weight_kg / (height_m ** 3)


#===== OUTPUTS =====
print(f"Body Surface Area: {bsa:.2f} square meters")
print(f"Ponderal Index: {ponderal_index:.2f}")