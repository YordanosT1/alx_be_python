#Tast 1. Shopping List Manager
shopping_list = [] #created empity list

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
display_menu()

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            value = input("Please add an item to add:") # Prompt for and add an item
            shopping_list.append(value)
            print(shopping_list)
            pass
        elif choice == '2':
            value = input("Please inert the value you want to remove: ")# Prompt for and remove an item
            shopping_list.remove(value)
            print(shopping_list)
            pass
        elif choice == '3':
            print(shopping_list)# Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()