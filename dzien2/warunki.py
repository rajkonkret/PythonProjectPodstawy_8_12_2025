# instrukcja warunkowa
# instrukcje sterowanie przepływem programu
# if
# w zależności od warunku wykona jeden lub drugi blok programu
# instrukcja w warunku musi zwrócić typ bool

odp = True

if odp: print("Test")
odp = False
if odp:
    print("brawo")
    print("brawo")
    print("brawo")
    print("brawo")
# Test
# brawo
# brawo
# brawo
# brawo
print("Dalsza cześc programu")

odp = "Radek"

if odp:
    print("Dane zostały wczytane")
# Dane zostały wczytane

if odp == "Radek":
    print("Jesteś Radek")  # Jesteś Radek

    odp = 0
if odp:
    print("Działą")
else:  # w przeciwym wypadku
    print("Zero -> False")
    # Zero -> False

a = "Radek"

if len(a) > 3:
    print(f"Długosć wynosi: {len(a)}, więcej niż 3")
# Długosć wynosi: 5, więcej niż 3

n = len(a)
if n > 3:
    print(f"Długosć wynosi: {n}, więcej niż 3")
    # Długosć wynosi: 5, więcej niż 3

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długosć wynosi: {n}, więcej niż 3")

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
#
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 40_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi: {zarobki * podatek} pln.")
# # od 10000 do 39999 podatek 0.2

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# operator warunkowy
rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi: {rabat}")  # Rabat wynosi: 25

# # napisąc test z...
# punktacja

punkty = 0
odp = input("Podaj date chrztu Polski")
# str
if odp == '966':
    print("Prawidłowa odpowiedź")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Odpowiedź nieprawidłowa")
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

odp = input("Czy Ala ma kota")
# str
if odp.strip().casefold() == 'tak'.strip().casefold():
    print("Prawidłowa odpowiedź")
    # punkty = punkty + 1
    punkty += 1
else:
    print("Odpowiedź nieprawidłowa")

print(f"Zdobyłeś  {punkty} pkt.")

slownik = {"Podaj date chrztu Polski": "966", "Czy Ala ma kota": "tak"}
lista_klucze = list(slownik.keys())

odp = input(lista_klucze[0])
if odp.strip().casefold() == slownik[lista_klucze[0]].strip().casefold():
    print("Odpowiedż prawidłowa")

# console, email, inny
alert_system = "console"
error_level = "error"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego.")
elif alert_system == "email":
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenia")
    else:
        lista_b.append("Inny")
    print("System email")
else:
    print("Inny system")

print(lista_b)
