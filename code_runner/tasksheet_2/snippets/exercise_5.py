# Write a conditional statement that decides whether the value of the int variable received from the console is even or odd.
#
# If the value is even, then the string "Value of variable <value of variable> is even!" should be output to the console. In case the value is odd, the output should be "Value of variable <value of variable> is odd!".
#
# Tip: use the modulo operator (%) to check if the remainder of division by 2 is 0.
#
# Zum Beispiel:
#
# Eingabe	Resultat
# 1
# Value of variable 1 is odd!
# 2
# Value of variable 2 is even!

number = int(input()) # Get number from user

if number % 2 == 0:
    print(f"Value of variable {number} is even!")
else:
    print(f"Value of variable {number} is odd!")