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

