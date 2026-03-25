n = int(input()) # Get the value of n from console


if n == 0:
    print(1) # 0!=1
else:
    result = 1
    for i in range(1, n + 1):
        result *= i

    print(result)