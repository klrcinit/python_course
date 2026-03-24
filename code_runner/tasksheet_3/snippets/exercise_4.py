# Write a program that reads in a positive variable named number and outputs the frequency of the digits it contains, from 9 to 0. Output the corresponding number only if the digit occurs at least once. Check out the given examples for the output format.
#
# Tip: Use number % 10 to get the last digit of the integer. Use number // 10 to truncate the last digit.
#
# Zum Beispiel:
#
# Eingabe	Resultat
# 505
# 5 occurs 2 time(s)
# 0 occurs 1 time(s)
# 324572
# 7 occurs 1 time(s)
# 5 occurs 1 time(s)
# 4 occurs 1 time(s)
# 3 occurs 1 time(s)
# 2 occurs 2 time(s)
# 927384923
# 9 occurs 2 time(s)
# 8 occurs 1 time(s)
# 7 occurs 1 time(s)
# 4 occurs 1 time(s)
# 3 occurs 2 time(s)
# 2 occurs 2 time(s)

number = int(input())

# create a list to count digits 0–9
count = [0] * 10

# count digits
while number > 0:
    digit = number % 10
    count[digit] += 1
    number = number // 10

# print from 9 to 0
for i in range(9, -1, -1):
    if count[i] > 0:
        print(f"{i} occurs {count[i]} time(s)")