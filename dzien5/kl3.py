class Car:
    """
    Klasa opisujaca samochód w pythonie
    """

    def __init__(self, model, year):
        """
        Konstruktor -metoda inicjalizująca
        :param model:
        :param year:
        """
        self.model = model
        self.year = year
        # pole ala prywatne
        # hermetyzacja
        self.__predkosc = 0

    # enkapsulacja - metody do zapisu i odczytu wartości pól
    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print("Prędkośc wynosi", self.__predkosc, "km/h.")

    def hamulec(self):
        self.__predkosc -= 10
        self.__zmien_bieg()

    def __zmien_bieg(self):
        print("Zmiana biegu")


car = Car("Łada", 2025)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# print(car.__predkosc)
# car.__predkosc = 0
car.licznik()
car.hamulec()
car.hamulec()
car.hamulec()
car.hamulec()
car.hamulec()
car.licznik()
# Prędkośc wynosi 0 km/h.
car.gaz()
car.licznik()
# Prędkośc wynosi 10 km/h.
car.__predkosc = 0
car.licznik()  # Prędkośc wynosi 10 km/h.
