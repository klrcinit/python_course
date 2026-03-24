# Write a for-loop that calculates and outputs the factorial of the number n.
#
# Tip: n! = n * (n - 1) * (n - 2) * ... * 1
#
# Note: Assume n >= 0
#
# Zum Beispiel:
#
# Eingabe: 2; 5	Resultat: 2, 120

n = int(input()) # Get the value of n from console

result = 1

for i in range(1, n + 1):
    result = result * i

print(result)