# Using a input() method,  int variables num1 and num2 and the float variable num3 are read from console.
#
# Perform the following calculations and store the results in the respected variable:
#
# 1. multiply: multiply num3 by num1
#
# 2. subtract: subtract num1 from 3 * num2
#
# 3.quotient_with_remainder: division num1 by num2
#
# 4.quotient_without_remainder: division num1 by num2
#
# 5.remainder: division num1 by num2
#
# 6.power: contains num2 to the fourth power.
#
# Tip: For the exponentiation (ab) please use the expression math.pow(a, b). For the division, pay attention to the data types!
#
# Zum Beispiel:
#
# Eingabe	Resultat
# 3
# 3
# 3
# 9.0
# 6
# 1.0
# 1
# 0
# 81.0

import math

num1 = int(input())
num2 = int(input())
num3 = float(input())

multiply = num3 * num1
subtract = (3 * num2) - num1
quotient_with_remainder = num1/num2
quotient_without_remainder= num1//num2
remainder = num1%num2
power = math.pow(num2, 4)


print(multiply)
print(subtract)
print(quotient_with_remainder)
print(quotient_without_remainder)
print(remainder)
print(power)

