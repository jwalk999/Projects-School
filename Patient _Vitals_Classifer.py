'''
Program: Patient_Vitals_Classifer.py
Author: Jonathan Walker
Date: 9/13/2026
Purpose: Use calculations and boolean logic to classify a patient's BMI and blood pressure
'''

#===== INPUTS =====
# convert to floating point decimals
# get weight in kilograms
weight_kg = float(input("Please enter the patient's weight in kilograms: "))
# get height in meters
height_m = float(input("Please enter the patient's height in meters: "))
# get systolic bp reading
systolic = float(input("Please enter the patient's systolic blood pressure: "))
# get diastolic bp reading
diastolic = float(input("Please enter the patient's diastolic blood pressure: "))


#===== PROCESS =====
# body mass index calculation
bmi = weight_kg / height_m ** 2

# body mass index classifier
if bmi >= 30:
    bmi_category = "Obese"
elif bmi >= 25:
    bmi_category = "Overweight"
elif bmi >= 18.5:
    bmi_category = "Normal"
else:
    bmi_category = "Underweight"
# boolean logic to categorize bmi, as calculated: weight / height ^ 2

# blood pressure classifier
if systolic >= 140 or diastolic >= 90:
    bp_category = "Stage 2"
elif systolic >= 130 or diastolic >= 80:
    bp_category = "Stage 1"
elif systolic >= 120 and diastolic < 80:
    bp_category = "Elevated"
else:
    bp_category = "Normal"
# boolean logic to categorize blood pressure, highest to lowest possible inputs

#===== OUTPUTS ======
# show BMI, 2 decimal places
print(f"BMI: {bmi:.2f}")
# show BMI category
print(f"BMI Category: {bmi_category}")
# show blood pressure category
print(f"Blood Pressure Category: {bp_category}")