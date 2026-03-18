# The values of the float variables num1 and num2 are read from the input. Swap the two values using a third float variable.
#
# Tip: triangle swap
#
# Question: why do we need a third variable to perform a swap?
#
# Zum Beispiel:
#
# Eingabe	Resultat
# 1
# 2
# 2.0
# 1.0

# Read a and b values
num1 = float(input())
num2 = float(input())

# Put your code here
temp = num1
num1 = num2
num2 = temp

print(num1)
print(num2)