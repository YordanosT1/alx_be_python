#Task: 1. Robust Division Calculator with Command Line Arguments
def safe_divide(numerator, denominator):
    try:
        numerators = float(numerator)
        denominators = float(denominator)
        div = numerators / denominators
        print(f"The result of the division is {div}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")