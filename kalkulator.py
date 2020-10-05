print("Witaj w kalkulatorze!")
print("1 - dodawanie "
      "2 - odejmowanie "
      "3 - mnożenie "
      "4 - dzielenie"
      "5 - potęgowanie)

x = input()
x = int(x)
if x == 1:
        print("pierwsza liczba: ")
        y1 = input()
        y1 = int(y1)

        print("druga liczba: ")
        y2 = input()
        y2 = int(y2)

        z = y1 + y2
        print(y1," + ",y2," = ",z)

elif x == 2:
        print("pierwsza liczba: ")
        y1 = input()
        y1 = int(y1)

        print("druga liczba: ")
        y2 = input()
        y2 = int(y2)

        z = y1 - y2
        print(y1, " - ", y2, " = ", z)

elif x == 3:
        print("pierwsza liczba: ")
        y1 = input()
        y1 = int(y1)

        print("druga liczba: ")
        y2 = input()
        y2 = int(y2)

        z = y1 * y2
        print(y1, " x ", y2, " = ", z)

elif x == 4:
        print("pierwsza liczba: ")
        y1 = input()
        y1 = float(y1)

        print("druga liczba: ")
        y2 = input()
        y2 = float(y2)

        z = y1 / y2
        print(y1, " : ", y2, " = ", z)
      
elif x == 5:
        print("liczba którą chcesz podnieść do potęgi: ")
        y1 = input()
        y1 = int(y1)

        print("potęga do której chcesz podnieść liczbę: ")
        y2 = input()
        y2 = int(y2)

        z = y1 ** y2

        print(y1," ^ ", y2, " = ", z)
      
else:
    print("zła liczba!")
