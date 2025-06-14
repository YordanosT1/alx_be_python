#Task: 1. Robust Division Calculator with Command Line Arguments
def safe_divide(numerator, denominator):
    try:
        numerators = float(numerator)
        denominators = float(denominator)
        div = numerators / denominators
        return f"The result of the division is {div}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."