#Task3. Drawing Patterns with Nested Loops
size = int(input("Enter the size of the pattern:"))
i = 0

while i <= size: 
    for j in range(0, size):
        print("*" * size, "\n", end="")
        #print("*" * size) removed it and used one print syntax
    break  # Exit the loop