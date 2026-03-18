# Three floating point numbers are read in. Decide whether these three numbers can form a triangle. If so, determine whether it is an equilateral, isosceles, or right triangle.
#
# Accordingly, print the following outputs:
#
#
#
# Condition
#
# Output
#
# No triangle
#
# "No triangle!"
#
# isosceles triangle
#
# "The three sides form an isosceles triangle!"
#
# equilateral triangle
#
# "The three sides form an equilateral triangle!"
#
# right triangle
#
# "The three sides form a right triangle!"

a = float(input())  # Get side a
b = float(input())  # Get side b
c = float(input())  # Get side c

# Najprej preverimo, ali sploh lahko nastane trikotnik
if a + b <= c or a + c <= b or b + c <= a:
    print("No triangle!")
else:
    # Equilateral (vse stranice enake)
    if a == b and b == c:
        print("The three sides form an equilateral triangle!")

    # Right triangle (Pitagorov izrek)
    elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print("The three sides form a right triangle!")

    # Isosceles (vsaj dve stranici enaki)
    elif a == b or a == c or b == c:
        print("The three sides form an isosceles triangle!")