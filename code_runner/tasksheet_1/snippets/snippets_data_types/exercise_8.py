# Familiarize yourself with Boolean operators and complete the following program.
#
# The given program prompts the user to enter the weather conditions by asking two questions: "Is it cold? (True/False)" and "Is it dry? (True/False)". The program also prompts the user to enter two integers.
#
# The program then stores the Boolean values and integers in separate variables: is_cold (True if it's cold, False otherwise), is_dry (True if it's dry, False otherwise), num1 (the first integer entered by the user), and num2 (the second integer entered by the user).
#
# You need to use the stored variables to calculate the following values: is_hot (True if it's not cold, False otherwise), is_cold_and_dry (True if it's both cold and dry, False otherwise), is_hot_or_dry (True if it's either hot or dry, or both, False otherwise), is_greater (True if num1 is greater than num2, False otherwise), and isEqual (True if num1 is equal to num2, False otherwise).
#
# Finally, print out the values of is_hot, is_cold_and_dry, is_hot_or_dry, is_greater, and is_equal, using the appropriate message for each value.
#
# Zum Beispiel:
#
# Eingabe	Resultat
# True
# False
# 5
# 4
# Is it cold? (True/False)
# Is it dry? (True/False)
# Is it hot? False
# Is it cold and dry? False
# Is it hot or dry? False
# Is the first number greater than second number? True
# Are the numbers equal? False

print("Is it cold? (True/False)")
is_cold = input() == "True"

print("Is it dry? (True/False)")
is_dry = input() == "True"

num1 = int(input())
num2 = int(input())

# TODO: Write your code here
is_hot =  not is_cold
is_cold_and_dry = is_cold and is_dry
is_hot_or_dry = not is_cold or is_dry
is_greater = num1 > num2
is_equal = num1 == num2

# Output results
print("Is it hot?", is_hot)
print("Is it cold and dry?", is_cold_and_dry)
print("Is it hot or dry?", is_hot_or_dry)
print("Is the first number greater than second number?", is_greater)
print("Are the numbers equal?", is_equal)

