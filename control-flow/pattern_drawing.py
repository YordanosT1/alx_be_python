#Task3. Drawing Patterns with Nested Loops
size = int(input("Enter the size of the pattern:"))
i = 0

while i <= size: 
    print(end="")
    for j in range(0, size):
        print("*" * size)
    break  # Exit the loop