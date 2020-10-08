products = ["Lion", "Mars", "Lays", "Ciastko", "Pepsi", "Cola", "Żelki", "Monster"]
price = ["0.5e", "0.75e", "1e"]

while True:
    print("Dzień dobry! Czy chciałbyś coś kupić? 1 = TAK, 0 = NIE")
    y = input()
    y = int(y)
    if y == 1:
        print("Wybierz numer produktu")
        for i, product in enumerate(products):
            print(i , product)

        x = input()
        x = int(x)

        if x == 0:
            print("Wybrałeś: {}".format(x), products[x], ", Należność: {}".format(price[0]))

        elif x == 1:
            print("Wybrałeś: {}".format(x), products[x], ", Należność: {}".format(price[0]))

        elif x == 2:
            print("Wybrałeś: {}".format(x), products[x], ", Należność: {}".format(price[1]))

        elif x == 3:
            print("Wybrałeś: {}".format(x), products[x], ", Należność: {}".format(price[1]))

        elif x == 4:
            print("Wybrałeś: {}".format(x), products[x], ", Należność: {}".format(price[1]))

        elif x == 5:
            print("Wybrałeś: {}".format(x), products[x], ", Należność: {}".format(price[1]))

        elif x == 6:
            print("Wybrałeś: {}".format(x), products[x], ", Należność: {}".format(price[2]))

        elif x == 7:
            print("Wybrałeś: {}".format(x), products[x], ", Należność: {}".format(price[2]))

        else:
            print("Artykuł niedostępny")

    print("Chcesz spróbować ponownie? 1 = TAK, 0 = NIE")
    z = input()
    z = int(z)

    if z == 0:
        break