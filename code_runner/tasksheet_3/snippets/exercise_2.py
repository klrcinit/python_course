# Write a while-loop which outputs the first n multiples of the number 7 (in ascending order) in one line and with one space between each.
#
# In addition, output the sum of all output numbers in the next line.
#
# Note 1: Assume that n > 0.
#
# Note 2: Do not worry about the space after the last number.
#
# Zum Beispiel:
#
# Eingabe	Resultat
# 2
# 7 14
# 21

# 5
# 7 14 21 28 35
# 105

n = int(input()) # Read value of n from the console

i = 1
total = 0

while i <= n:
    value = 7 * i
    print(value, end=" ")
    total = total + value
    i = i + 1

print()
print(total)

