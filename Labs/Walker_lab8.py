"""
Lab 8: Patient Records File Processor (File Handling)
CIS 3680
Starter file. Fill in the TODOs. Do not change the output format, your
output file is graded against it line by line.
"""


def calculate_bmi(weight_lbs, height_in):
    """Return BMI given weight in pounds and height in inches."""
    return (weight_lbs / (height_in ** 2)) * 703


def load_patients(filename):
    """Read patient_records.csv and return a list of patient dicts.

    Skips the header row and any blank lines. Strips whitespace from
    every field, every record in the file has extra spaces somewhere.
    """
    patients = []
    
    # Open and read csv file, each line contains 1 list
    with open(filename) as file:
        lines = file.readlines()

    for line in lines[1:]:
        # Skip blank lines
        if line.strip() == "":
            continue

        # Split with commas, then strip white space
        fields = [piece.strip() for piece in line.split(",")]
        # Create dicts
        patient = {
            "patient_id": fields[0],
            "name": fields[1],
            "age": fields[2],
            "weight_lbs": int(fields[3]),
            "height_in": int(fields[4]),
            "condition": fields[5] or "Not specified", # If condition key is empty
        }
        patients.append(patient)

    return patients


def main():
    patients = load_patients("patient_records.csv")

    bmis = []
    summary_lines = []

    # Add counter, average bmi, highest bmi, and lowest bmi variables
    patients_processed = 0
    highest_bmi = None
    highest_name = ""
    lowest_bmi = None
    lowest_name = ""
    for patient in patients:
        
        # Use calculate_bmi function by plugging in each individual weight and height
        bmi = calculate_bmi(patient["weight_lbs"], patient["height_in"])
       # Put it in the list
        bmis.append(bmi)
       
        # Create display name 'Last First'
        display_name = patient["name"].title()
        if patient["condition"] == "Not specified":
            condition_case = "Not specified"
        else:
            condition_case = patient["condition"].title()

        summary_line = f"{display_name}, Age {patient['age']}, BMI {bmi:.1f}, Condition {condition_case}"
        
        # 1 patient processed, add to counter
        patients_processed += 1

        # BMI boolean logic
        if highest_bmi is None or bmi > highest_bmi:
            highest_bmi = bmi
            highest_name = display_name
        if lowest_bmi is None or bmi < lowest_bmi:
            lowest_bmi = bmi
            lowest_name = display_name

        lowest_bmi = min(bmis)
        average_bmi = sum(bmis) / len(bmis)
        summary_lines.append(summary_line)

    with open("patient_summary.txt", "w") as f:
        f.writelines("\n".join(summary_lines) + "\n")
        f.writelines(f"\nPatients Processed: {patients_processed}\n")
        f.writelines(f"Average BMI: {average_bmi:.1f}\n")
        f.writelines(f"Highest BMI: {highest_name} ({highest_bmi:.1f})\n")
        f.writelines(f"Lowest BMI: {lowest_name} ({lowest_bmi:.1f})\n")




    print(f"Wrote summary for {len(patients)} patients to patient_summary.txt")


if __name__ == "__main__":
    main()
