#Task 2. Explore `datetime` Module
import datetime 
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now() # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S") 
    print(f"Current date and time: {formatted_date}")
    # print(current_date) # Print the current date and time
display_current_datetime()

def calculate_future_date(): #Create a function with a name calculate_future_date
    current_date = datetime.datetime.now() # Get the current date and time
    future_date = int(input("Enter the number of days to add to the current date:")) #Prompt the user to enter a number of days (as an integer).
    time_delta = timedelta(days=future_date) #timedelta: This object represents a duration. You can specify days, hours, minutes, seconds, weeks, etc.
    future_date = current_date + time_delta #future date
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date: {formatted_date}")
    #print("Future Date:", future_date) #printing the futur date
calculate_future_date()
