#Task 2. Multiplication Table Generator

#Prompt User for a Number
number = int(input("Enter a number to see its multiplication table:"))

#Generate and Print the Multiplication Table
for i in range(1, 11):
    table = number * i
    print(f"{number} * {i} = {table}")