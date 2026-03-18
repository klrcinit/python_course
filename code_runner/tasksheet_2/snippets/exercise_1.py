# An age variable is read from the console as an integer. Print the associated age category according to the following table. Use the if statement for this. The error text "Input is invalid!" should be printed if the input is out of range.
#
# Age range	Category
# 0-12	Child
# 13-19	Teen
# 20-59	Adult
# 60-120	Senior
# Note: All the boundaries are inclusive. For example, age 12 prints "Child" and 120 prints "Senior".


age = int(input())

if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60 and age <= 120:
    print("Senior")
else:
    print("Input is invalid!")

