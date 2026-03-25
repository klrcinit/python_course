number = int(input())

# 169990
for i in range(9, -1, -1): # i: 9
    num = number # num: 1699
    count = 0 # count:0

    #  loop for one digit [9, ..., 1]
    while num > 0:
        digit = num % 10 # digit 9
        num //= 10

        if digit == i:
            count += 1


    if count > 0:
        print(f"{i} occurs {count} time(s)")
