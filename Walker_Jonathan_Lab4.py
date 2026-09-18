'''
Program: Walker_Jonathan_Lab4.py
Author: Jonathan Walker
Date: 9/18/2026
Purpose: Use sentinel controlled while loops to classify a batch 
            of patient's vitals
'''

#===== INPUT =====
# prompt user to input weight, if user enters number: begin loop
# if user enters nothing: end loop
weight_input = input("Enter patient weight in kg (or press Enter to stop): ")
patient_count = 0  # count the number of patients processed
total_bmi = 0
# begin while loop
while weight_input!= "":
    weight_kg = float(weight_input)
    height_m = float(input("Enter patient height in meters: "))
    systolic = float(input("Enter patient systolic blood pressure: "))
    diastolic = float(input("Enter patient diastolic blood pressure: "))
    patient_count += 1 # add 1 patient to counter

#===== PROCESS =====
    # calculate patient bmi
    bmi = weight_kg / height_m ** 2
    # classify bmi category
    if bmi >= 30:
        bmi_category = "Obese"
    elif bmi >= 25:
        bmi_category = "Overweight"
    elif bmi >= 18.5:
        bmi_category = "Normal"
    else:
        bmi_category = "Underweight"    

    # classify blood pressure category
    if systolic >= 140 or diastolic >= 90:
        bp_category = "Stage 2"
    elif systolic >= 130 or diastolic >= 80:
        bp_category = "Stage 1"
    elif systolic >= 120 and diastolic < 80:
        bp_category = "Elevated"
    else:
        bp_category = "Normal"
    # add previous patient's BMI to running total
    total_bmi += bmi

#===== OUTPUT =====
    print(
        f"Patient {patient_count}:\nBMI: {bmi:.2f} ({bmi_category})\n"
        f"Blood Pressure: {bp_category}"
    )
    # start loop over from the top
    weight_input = input(
        "\nEnter patient's weight in kg (or press Enter to stop): "
        )

# get average of all bmi values
average_bmi = total_bmi / patient_count
print(f"Average BMI: {average_bmi:.2f}")
print(f"Patients processed: {patient_count}")
