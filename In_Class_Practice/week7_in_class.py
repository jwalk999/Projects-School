# Build a function that has a two-sided range guard for a thermostat.
# Desired temp should display acceptable message with the degrees
# however, if below 32F or above 90F, you should get a warning

def check_temp_range(temperature_reading=float) -> float:
    """
    Check the reading of a thermostat to see if it is acceptable

    Args:
        temperature_reading: user inputs the reading

    Returns: 
        acceptable_temperature: If the temp is within the defined range

    """
    if temperature_reading < 32:
        return "Too Cold!"
    elif temperature_reading > 90:
        return "Too Hot!"
    else:
        return "Just Right!"

temperature_reading = float(input("Enter thermostat reading: "))

while temperature_reading != "":
    print(f"check_temp_range(temperature_reading): {check_temp_range(temperature_reading)}")
    temperature_reading = float(input("Enter thermostat reading: "))