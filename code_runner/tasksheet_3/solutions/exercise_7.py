# Write a while-loop that calculates Fibonacci number Fn. Fibonacci numbers are calculated as follows:
#
# F0 = 0, F1 = 1, F{n} = F{n-2} + F{n-1}
#
# For more detailed information, the English Wikipedia article is recommended.
#
# https://en.wikipedia.org/wiki/Fibonacci_sequence
#
# Note: For invalid input values for number (i.e., negative values) output the string "Invalid".
#
# Zum Beispiel:
#
# Eingabe:	Resultat
# -1 --> Invalid
# 2 --> 0 1 1
# 5 --> 0 1 1 2 3 5

n = int(input()) # Get value of n from the console

if n < 0:
    print("Invalid")
else:
    a, b = 0, 1
    i = 0

    while i <= n:
            print(a, end=" ")
            c = a + b
            a = b
            b = c
            i = i + 1