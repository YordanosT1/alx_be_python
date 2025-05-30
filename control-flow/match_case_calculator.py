#Task 1. Simple Calculator with Match Case

#propt user to enter the 2 numbers and operations they want to be excuted (calculated).
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operations = str(input("Choose the operation (+, -, *, /):"))

#calculator
addition = num1 + num2
subtract = num1 - num2
multiply = num1 * num2


#Performing the Calculation Using Match Case
match operations:
    case "+":
          print("The result is", addition, end='')
          print(".")
    case "-":
          print("The result is", subtract, end='')
          print(".")
    case "*":
          print("The result is", multiply, end='')
          print(".")
    case "/":
            if num2 == 0:
                  print("Cannot divide by zero")
            else:
                  divide = num1 / num2
                  print("The result is", divide, end='')
                  print(".")
    case _:
            print("syntax error")