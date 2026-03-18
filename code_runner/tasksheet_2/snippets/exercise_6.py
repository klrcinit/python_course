# The grade from the input (as a string variable from A to F) is read. Using the match statement specify the corresponding description of the grade according to the table below. For example, the output should be "Excellent" for the value "A". The error text "Invalid grade!" should be output if the input is incorrect.
#
#
#
# Grade
#
# Description
#
# A
#
# Excellent
#
# B
#
# Good
#
# C
#
# Fair
#
# D
#
# Unsatisfactory
#
# E
#
# Unsatisfactory
#
# F
#
# Failed
#
#
#
# Note: The use of the match statement is necessary, we do not allow other branching structures for this task.

grade = input() # Get input from the user

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Fair")
    case "D" | "E":
        print("Unsatisfactory")
    case "F":
        print("Failed")
    case _:
        print("Invalid grade!")