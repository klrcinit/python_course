# The value for the int variable hour (a number in the range of [0,24]) is read from the console using the input() function. Print the following results based on the value. For example: If the value of hour variable is greater or equal to 6 and less than or equal to 12, print a "Good morning" greeting, using if statements.
#
# If the input doesn't fit any of the ranges, print "Good day".
#
# Hour
#
# Greeting
#
# 6-12
#
# Good morning
#
# 13 - 15
#
# Good afternoon
#
# 16 - 18
#
# Good evening
#
# 19 - 23
#
# Good night
#
# Note: The ranges include the numbers themselves.
#
# Zum Beispiel:
#
# Eingabe	Resultat
# -5
# Good day
# 12
# Good morning

hour = int(input())

if hour >= 6 and hour <= 12:
    print("Good morning")
elif hour >= 13 and hour <= 15:
    print("Good afternoon")
elif hour >= 16 and hour <= 18:
    print("Good evening")
elif hour >= 19 and hour <= 23:
    print("Good night")
else:
    print("Good day")