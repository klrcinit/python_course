# Write a program that reads a day_of_week as an input (a string variable from "Monday" to "Sunday") using input() function. Using the match statement, output the type of the day according to the table below. For example, the output should be "Weekday" for the value "Tuesday". The error message "Invalid day!" should be displayed if the input is incorrect.
#
# Day
#
# Description
#
# Monday
#
# Weekday
#
# Tuesday
#
# Weekday
#
# Wednesday
#
# Weekday
#
# Thursday
#
# Weekday
#
# Friday
#
# Weekday
#
# Saturday
#
# Weekend
#
# Sunday
#
# Weekend
#
#
#
# Note: The use of the match statement is necessary, we do not allow other branching structures in this task.

day_of_week = input()  # Get input from the user

match day_of_week:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Invalid day!")