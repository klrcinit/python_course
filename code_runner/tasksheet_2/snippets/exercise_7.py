# Convert the given match statement into an equivalent if-elif-else statement.
# match month:
#     case 1 | 2 | 3:
#         quarter_string = "first quarter"
#     case 4 | 5 | 6:
#         quarter_string = "second quarter"
#     case 7 | 8 | 9:
#         quarter_string = "third quarter"
#     case 10 | 11 | 12:
#         quarter_string = "fourth quarter"
#     case _:
#         quarter_string = "invalid month"

month = int(input()) # Get input from the user

if month == 1 or month == 2 or month == 3:
    quarter_string = "first quarter"
elif month == 4 or month == 5 or month == 6:
    quarter_string = "second quarter"
elif month == 7 or month == 8 or month == 9:
    quarter_string = "third quarter"
elif month == 10 or month == 11 or month == 12:
    quarter_string = "fourth quarter"
else:
    quarter_string = "invalid month"

print(quarter_string)
