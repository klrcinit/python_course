# Read the three int variables start, stop and step using input() function. For the test cases, you can assume that stop ≥ start and step > 0.
#
# Now write a for-loop that starts with the value of start. Increase the loop variable by step in each step and end the loop until the value of stop (inclusive) is reached. In the loop, output the value of the loop variable unless it is a multiple of 3. If the variable is a multiple of 3, output the string "HOP" instead of the number. Output your results in one line, using spaces to separate the numbers. Follow the format defined in the sample table.
#
# Note: Do not worry about the space after the last number.
#
# Zum Beispiel:
#
# Eingabe	Resultat
# 1
# 4
# 1
# 1 2 HOP 4
# 0
# 10
# 1
# HOP 1 2 HOP 4 5 HOP 7 8 HOP 10

start = int(input())
stop = int(input())
step = int(input())

for i in range(start, stop + 1, step):
    if i % 3 == 0:
        print("HOP", end=" ")
    else:
        print(i, end=" ")