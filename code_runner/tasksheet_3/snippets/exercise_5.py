# Read the int variable number using input()function. Output the numbers number to 1 in one line (with one space between them).
#
# In the next line, output the numbers -number to number (with one space between them).
#
#
#
# Note 1: Use while loop and follow the format in the table for the output.
#
# Note 2: Do not worry about the space after the last number.
#
# Note 3: If number ≤ 0, print "Invalid input!"
#
# Zum Beispiel:
#
# Eingabe	Resultat
# -1 --> Invalid input!
# 3 --> 3 2 1
#       -3 -2 -1 0 1 2 3


number = int(input())

if number <= 0:
    print("Invalid input!")
else:
    # Line 1: number → 1
    i = number
    while i >= 1:
        print(i, end=" ")
        i = i - 1

    print()  # new line

    # Line 2: -number → number
    i = -number
    while i <= number:
        print(i, end=" ")
        i = i + 1