# Use the input() method to get input from the user.
# Assume that the input is in the order of name, family name, age, and salary.
#
# For example
#
# "Hannah
#
# Mayr
#
# 24
#
# 1234.5"
#
# When reading in, assign the values to the variables first_name, family_name, age, and salary, respectively.
#
# Note:
#
# ·         The input() function is used to take user input from the keyboard.
#
# ·         It always returns the entered data as a string.
#
# Zum Beispiel:
#
# Eingabe	Resultat
# Hannah
# Mayr
# 24
# 1234.5
# Hannah
# Mayr
# 24
# 1234.5

first_name = input()
family_name = input()
age = int(input())
salary = float(input())

print(first_name)
print(family_name)
print(age)
print(salary)