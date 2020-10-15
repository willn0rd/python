

while True:
    kosztystale = int(input("Ile wynoszą koszty stałe?: "))
    kjz = int(input("Ile wynoszą koszty zmienne?: "))
    cjz = int(input("Ile wynosi cena za jednostke?: "))


    def oblicz_BEP(kosztystale, kjz, cjz):
        return (kjz - cjz) / kosztystale


    wynik = oblicz_BEP(kosztystale, kjz, cjz)

    print("PROGRAM DO LICZENIA BEP")
    if kosztystale > 0:
        print("BEP wynosi:", wynik)
        x = int(input("Aby uruchomić program ponownie wpisz 1, aby zamknąć działanie programu wpisz 2: "))
        if x == 0:
            break

    else:
        print("Koszty stałe mniejsze niż 0!")
        x = int(input("Aby uruchomić program ponownie wpisz 1, aby zamknąć działanie programu wpisz 2: "))
        if x == 0:
            break





