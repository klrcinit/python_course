number = int(input())

if number <= 0:
    print('Invalid input')

else:
    # Line 1: number → 1
    i = number
    while i != 0:
        print(i, end=' ')
        i -= 1

    print()  # new line

    # Line 2: -number → number
    n = -number # lahko je tudi i
    while n != number+1:
        print(n, end=' ') # lahko je tudi i
        n += 1