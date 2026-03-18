# Implement an ATM. An amount of money is entered, divide this amount into the smallest possible number of bills (i.e., bills with a higher amount of money are preferred). The bills available in your ATM are 100, 50, 20, 10, 5.
#
# Since there are no coins, you must also check whether the amount entered can be processed at all. If this is not the case, issue an error message: "Enter amount cannot be processed!"
#
# Tip: Use the operators // and %.
#
#
#
# Zum Beispiel:
#
# Eingabe	Resultat
# 159
# Enter amount cannot be processed!
# 290
# 100 Euro: 2
# 50 Euro: 1
# 20 Euro: 2
# 35
# 20 Euro: 1
# 10 Euro: 1
# 5 Euro: 1

money = int(input()) # Get input from the user

# Najprej preverimo, če je možno razbiti znesek (brez kovancev)
if money % 5 != 0:
    print("Enter amount cannot be processed!")
else:
    # Razdelimo na bankovce (od največjega proti najmanjšemu)
    hundreds = money // 100
    money = money % 100

    fifties = money // 50
    money = money % 50

    twenties = money // 20
    money = money % 20

    tens = money // 10
    money = money % 10

    fives = money // 5

    # Izpis (samo če je > 0)
    if hundreds > 0:
        print("100 Euro:", hundreds)
    if fifties > 0:
        print("50 Euro:", fifties)
    if twenties > 0:
        print("20 Euro:", twenties)
    if tens > 0:
        print("10 Euro:", tens)
    if fives > 0:
        print("5 Euro:", fives)