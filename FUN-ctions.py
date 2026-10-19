# squaring a number, 1 specific number

# Arithmetic
x = 5
y = (x ** 2)
print(y)

# Mult by itself
x = 5
y = (x * x)
print(y)

# F strings
x = 5
y = (x * x)
print(f"5 Squared: {y}")

# function
def y(number: float) -> float:
    """Return a number multiplied by itself."""
    return number * number

print(f"square(5): {y(5)}")
print(f"square(12): {y(12)}")

# Example 2 - Temperature Conversion
celcius = 20
fahrenheit = celcius * 9 / 5 + 32
print(f"20C in Fahrenheit: {fahrenheit}")

# as a function
def celcius_to_fahrenheit(celcius: float) -> float:
    """Convert Celcius to Fahrenheit"""
    return celcius * 9 / 5 + 32

# Print 20, 0, 100
print(f"Celcius to Fahrenheit(20): {celcius_to_fahrenheit(20)}")
print(f"Celcius to Fahrenheit(0): {celcius_to_fahrenheit(0)}")
print(f"Celcius to Fahrenheit(100): {celcius_to_fahrenheit(100)}")


# Example 3 - Area of a Rectangle

length = 20
width = 5
area = length * width
print(area)

# As a function
def calculate_area(length: float, width: float) -> float:
    """Return the Area of a Rectangle"""
    return length * width
print(f"Rectangle Area(L20, W5): {calculate_area(20, 5)}")


# Example 5 - Building a greeting
name = "Bob"
greeting = "Hello " + name +"!"
print(greeting)

# as a function
def build_greeting(name: str) -> str:
    """Return a greeting"""
    return f"Hello, {name}!"
print(build_greeting("Sam"))
name_input = input("What is your name?: ")
print(build_greeting(name_input))