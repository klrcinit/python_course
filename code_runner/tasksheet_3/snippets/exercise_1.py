# Write a for-loop which outputs the numbers 1 to n in one line and with one space between each.
#
# Tip: familiarize yourself with the sep and end parameters in the print function
#
# Zum Beispiel:
#
# Eingabe:2; 5	Resultat: 1 2 ; 1 2 3 4 5;

n = int(input()) # Read the value of n from the console

for i in range(1, n + 1):
    print(i, end=" ")