from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa Ptak opsiująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością:", self.szybkosc, "km/h")

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    klasa Kura dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        # obowiązkowo musi być wywołany konstruktor kalsy wyższej
        super().__init__(gatunek, 0)

    def latam(self):
        print(f"Tu {self.gatunek}, Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko")


class Orzel(Ptak):

    def wydaj_odglos(self):
        print("kier kir kier")


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
#
# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością: 45 km/h
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością: 0 km/h

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura, Ja nie latam.

or2 = Orzel("Orzel Bielik", 50)
or2.latam()
or2.wydaj_odglos()
# Tu Orzel Bielik Lecę z szybkością: 50 km/h
# kier kir kier

lista = [kur2, or2]
# polimorfizm - obiekty różnych klas mają cechy wspólne
for i in lista:
    i.wydaj_odglos()
