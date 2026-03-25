
number = int(input()) # Read number from the console

while number > 0:
    last = number % 10
    print(last, end="")
    number = number // 10