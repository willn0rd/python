import random

x = random.randrange(1,21)

i = 0
print("Podaj liczbę z zakresu 1 - 20: ")
while i != x:
    i = input()
    i = int(i)
    if i == x:
        print("Gratulacje!")

    elif i > 20:
        print("Zbyt duża liczba! Wybierz jakąś z przedziału 1 - 20")

    elif i < 1:
        print("Zbyt mała liczba! Wybierz jakąś z przedziału 1 - 20")

    else:
        print("Wybierz inną liczbę!")
