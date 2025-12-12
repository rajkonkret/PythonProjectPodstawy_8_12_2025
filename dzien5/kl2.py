class Human:
    """
    Klasa  Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def __str__(self):
        return f"{self.imie} {self.wiek} {self.wzrost} {self.plec}"


# TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
# cz1 = Human()

cz1 = Human("Radek", 45, 189, "m")
print(cz1.wzrost)
print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)
# 189
# 45
# Radek
# m
print(cz1)
# pododpisaniu __str__
# Radek 45 189 m

cz1.wypisz_wzrost()
cz1.wypisz_wiek()
# Mam 189 cm wzrostu.
# Mam 45 lat.
