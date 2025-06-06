#Task 4. Personal Daily Reminder
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        print("This task is important that requires immediate attention today!")
    case "medium":
        print("This task is moderately important that requires attention")
    case "low":
        print("This task is not as important but can be deligated.")
    case _:
       print("Please specify your tasks again")

if time_bound == "yes":
    print("Reminder:", task, "is a high priority task that requires immediate attention today!")
else:
    print("Note:", task, "is a low priority task. Consider completing it when you have free time.")