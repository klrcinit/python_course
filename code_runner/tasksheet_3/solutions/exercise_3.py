start = int(input())
stop = int(input())
step = int(input())

for i in range(start, stop + 1, step):
    if i % 3 == 0:
        print("HOP", end=" ")
    else:
        print(i, end=" ")