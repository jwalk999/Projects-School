"""
Lab 9: Patient Record Validation
CIS 3680, Prof. Taylor

Reads patient_records_lab9.csv, validates each record (patient ID format,
missing fields, numeric conversion, range checks), calculates BMI and
classification for valid records, and reports the results.
"""

import csv
import re

PATIENT_ID_PATTERN = r"^P-\d{4}$"

FIELD_RANGES = {
    "age": (0, 120),
    "weight_lbs": (1, 600),
    "height_in": (1, 96),
}


def validate_patient_id(patient_id: str) -> bool:
    """Return True if patient_id matches the P-#### format, False otherwise."""
    if re.fullmatch(PATIENT_ID_PATTERN, patient_id):
        return True
    else:
        return False


def validate_field(field_name: str, raw_value: str) -> float:
    """
    Convert and range-check a single numeric field.

    Raises ValueError if the field is missing, non-numeric, or out of range.
    Returns the converted numeric value if valid.
    """
    # 'raw_value' is entered as a string, it should not be empty.
    if not raw_value or raw_value.strip() == "":
        raise ValueError(f"{field_name} was not entered.")

    try:
        value = float(raw_value)
    except ValueError:
        raise ValueError(f"{raw_value} is not a valid entry to {field_name}")

    low, high = FIELD_RANGES[field_name]
    if low <= value <= high:
        return value
    else:
        raise ValueError(f"{raw_value} is out of range for {field_name}.")


def calculate_bmi(weight_lbs: float, height_in: float) -> float:
    """Return BMI using the standard imperial formula."""
    return (weight_lbs / (height_in**2)) * 703


def classify_bmi(bmi: float) -> str:
    """Return the weight classification for a given BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


def process_record(record: dict) -> dict:
    """
    Validate and process one patient record.

    Returns a dict with keys:
      "status": "ok" or "flagged"
      "patient_id": the ID (or "UNKNOWN" if the ID itself was invalid)
      and either ("name", "bmi", "classification") on success
      or ("reason",) on failure.
    """
    if not validate_patient_id(record["patient_id"]):
        return {
            "status": "flagged",
            "patient_id": "UNKNOWN",
            "reason": f"Invalid patient ID {record.get('patient_id')}",
        }

    name = record.get("name")
    patient_id = record["patient_id"]
    if name is None or name.strip() == "":
        return {
            "status": "flagged",
            "patient_id": str(patient_id),
            "reason": "Name not entered",
        }

    try:
        age = validate_field("age", record.get("age"))
        weight_lbs = validate_field("weight_lbs", record.get("weight_lbs"))
        height_in = validate_field("height_in", record.get("height_in"))
    except ValueError as e:
        return {"status": "flagged", "patient_id": str(patient_id), "reason": str(e)}

    # Call calculate_bmi function to store in the dict
    bmi = calculate_bmi(weight_lbs, height_in)
    return {
        "status": "ok",
        "patient_id": str(patient_id),
        "name": str(name),
        "bmi": bmi,
        "classification": classify_bmi(bmi),
    }


def main() -> None:
    """Read the roster, process every record, and print the report."""
    ok_count = 0
    flagged_count = 0

    with open("patient_records_lab9.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for record in reader:
            result = process_record(record)

            if result["status"] == "ok":
                ok_count += 1
                print(
                    f"{result['patient_id']} - {result['name']}: "
                    f"BMI {result['bmi']:.1f} ({result['classification']})"
                )
            else:
                flagged_count += 1
                print(f"{result['patient_id']} - FLAGGED: {result['reason']}")

    print()
    print(f"Summary: {ok_count} processed successfully, {flagged_count} flagged.")


if __name__ == "__main__":
    main()
