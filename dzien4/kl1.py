# klasa - szablon, przepis
# cechy (zmienne)
# metody - funkcje w klasie
# obiekt - instancja kalsy
# klasa musi być najpierw zadeklarowana
# tworzenie obiektu uruchamia metode inicjalizującą (konstruktor) __init__
# paradygmaty - hermetyzacja, dziedziczenie, polimorfizm, abstrkcja

# n PascalCase, UpperCamelCase
class Human:
    """
    Klasa Human opisująca czlowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się: {self.imie}")

    def ruszaj(self):

        if self.plec =="m":
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę.")


print(Human.__doc__)  # Klasa Human opisująca czlowieka w pythonie
# print(print.__doc__)
# cd .. katalog wyżej
# cd dzien4
# pydoc -b  - serwer
# pydoc -w kl1 - plik html

# tworzenie obiektu klasy Human
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x107fee270>

print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)

cz1.imie = "Radek"
cz1.wiek = 50
cz1.plec = "m"
print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)
# 50
# Radek
# m
cz1.powitanie()
#  Nazywam się: Radek

cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 34

print(cz2.wiek)
print(cz2.imie)
print(cz2.plec)
cz2.powitanie()
# Nazywam się: Anna
