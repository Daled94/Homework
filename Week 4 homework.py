#15 Use the DateTime module to get Current Date and Time, and save it to a variable. Then extract just the Full month name form that variable.

import datetime

current_datetime = datetime.datetime.now()

full_month_name = current_datetime.strftime("%B")

print("Current date and time:", current_datetime)
print("Full month name:", full_month_name)

#16. Write a simple function that takes 2 parameters -- a first name and a day name.
def greet_with_day(first_name, day_name="Sunday"):
    greeting = f"Hi {first_name}! Happy {day_name}!"
    print(greeting)

greet_with_day("Alice", "Wednesday")
greet_with_day("Bob", "Friday")

greet_with_day("Charlie")


#17. Write a block of code to handle one of the most common Python exception errors. Select one of the common errors from the curriculum section on Python Exception handling. Have your code example uses the try,except, else, and finally components.

try:
    user_input = input("43:-17 ")
    number = int(user_input)
    print("You entered:", number)
