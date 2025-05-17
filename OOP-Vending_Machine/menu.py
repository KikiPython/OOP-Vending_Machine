from items import items

print("Availible items:")
print("A1: Chips - $1.50 ({chips.amount} left)")
print("B2: Candy - $1.25 ({candy.amount} left)")
print("C3: Soda = $1.00 ({soda.amount} left)")

ci = input("Enter code to buy (or 'exit'): ")
#ci = chosen item

if ci = ("A1"):
    money1 = input(int("Insert money ($): "))
    if money1 <= 1.49:
        print("Not enough money inserted!")
    if money1 >= 1.50:
        print("Inserted: {money1}")
        money1 - 1.50 = change1before
        #"whole loop"
        if change1before >= quarter:
            change1before % quarter = change1
        elif change1before >= dime:
            change1before % dime = change1
        elif change1before >= nickel:
            change1before % nickel = change1
        elif change1before >= cent:
            change1before % cent = change1
        else:
            #"ends whole loop"
        print("Dispensed Chips")
        print("Change: {change1}")
    else:
        print("Not a number!")

elif ci = ("B2"):
    money2 = input(int("Insert money ($): "))
    if money2 <= 1.24:
        print("Not enough money inserted!")
    if money2 >= 1.25:
        print("Inserted: {money2}")
        money2 - 1.25 = change2before
        #"whole loop"
        if change2before >= quarter:
            change2before % quarter = change2
        elif change2before >= dime:
            change2before % dime = change2
        elif change2before >= nickel:
            change2before % nickel = change2
        elif change2before >= cent:
            change2before % cent = change2
        else:
            #"ends whole loop"
        print("Dispensed Candy")
        print("Change: {change2}")
    else:
        print("Not a number!")

elif ci = ("C3"):
    money3 = input(int("Insert money ($): "))
    if money3 <= 0.99:
        print("Not enough money inserted!")
    if money3 >= 1.00:
        print("Inserted: {money3}")
        money3 - 1.00 = change3before
        #"whole loop"
        if change3before >= quarter:
            change3before % quarter = change3
        elif change3before >= dime:
            change3before % dime = change3
        elif change3before >= nickel:
            change3before % nickel = change3
        elif change3before >= cent:
            change3before % cent = change3
        else:
            #"ends whole loop"
        print("Dispensed Soda")
        print("Change: {change3}")
    else:
        print("Not a number!")