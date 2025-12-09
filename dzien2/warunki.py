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
