n = int(input()) # Read value of n from the console

i = 1
sum = 0

while i <= n: #vedno mas conditions
    value = 7 * i
    print(value, end=" ")
    sum = sum + value
    i = i + 1

print()
print(sum) # mas tut opcijo formata f(´\n{sum}´)