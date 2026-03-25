# Write a for-loop that calculates Fibonacci number Fn. Fibonacci numbers are calculated as follows:
#
# F0 = 0, F1 = 1, F{n} = F{n-2} + F{n-1}
#
# For more detailed information, the English Wikipedia article is recommended.
#
# https://en.wikipedia.org/wiki/Fibonacci_sequence
#
# Note: For invalid input values for number (i.e., a negative value) print "Invalid input!".
#
# Zum Beispiel:
#
# Eingabe	Resultat
# 2 --> 1
# 5 --> 5
# -1 --> invalid input!

number = int(input())  # Read an integer number as a input from the user / console

if number < 0:
    print("Invalid input!")
elif number == 0 or number == 1:
    print(number)
else:
    f0 = 0
    f1 = 1
    fn = 0

    for i in range(2, number + 1):
            fn = f0 + f1
            f0 = f1
            f1 = fn
            print(fn)