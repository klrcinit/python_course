number = int(input())

#while True:
  #  n =input() #  run input from user forever
  #  print(n)

while True:
    n = input("Enter the value, and enter 'quit' if you want to exit: ")
    if n == 1:
        continue
    if n == 'quit':
         break # outside of the loop it will never be reached
    print(n)

print("end!")

