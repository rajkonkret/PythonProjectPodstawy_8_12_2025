# pętla - pozwala wielokrotnie wykonac fragment kodu
# for - pętla iteracyjna
import random

for i in range(5):  # 0 do 4
    print(i)

for i in range(20):
    pass  # nic nie rob

for _ in range(10):  # niema zmienna
    print("Test podłogaa")
    print(_)
    # Test podłogaa
    # 9

for i in range(5):
    print(i + 2)
    print(i * 2)

# przerobic lotto na petle
lista_kule = list(range(1, 50))
lista_wynik = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    print(wyn)
    lista_wynik.append(wyn)

print(lista_wynik)  # [19, 41, 8, 36, 34, 42]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")

# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# parzyste do nowej listy
lista_parzyste = []
for j in range(10):
    if j % 2 == 0:
        lista_parzyste.append(j)

print(lista_parzyste)  # [0, 2, 4, 6, 8]

# list comprehensions
lista_parzyste = [j for j in range(10) if j % 2 == 0]
print(lista_parzyste)  # [0, 2, 4, 6, 8]

for i in range(1, 10):
    print(i)

for c in lista_parzyste:  # dla wszystkich elementów kolekcji
    print(c)

lista_nazwy = ["Ala", "Tomek", "Zenek", "Basia"]

for p in lista_nazwy:
    print(p)  # kolejne elementy listy
# Ala
# Tomek
# Zenek
# Basia

for c in lista_parzyste:
    if c > 4:
        print(c, "Większe od 4")
    elif c == 4:
        print(c, "Równe 4")
    else:
        print(c, "Mniejsze od 4")
    print("Dla kazdego przejscia pętli", c)
print("Po zakończeiu pętli")
# 0 Mniejsze od 4
# Dla kazdego przejscia pętli 0
# 2 Mniejsze od 4
# Dla kazdego przejscia pętli 2
# 4 Równe 4
# Dla kazdego przejscia pętli 4
# 6 Większe od 4
# Dla kazdego przejscia pętli 6
# 8 Większe od 4
# Dla kazdego przejscia pętli 8
# Po zakończeiu pętli

for i in range(10, 0, -2):  # start, stop, krok, -2, odliczanie w dół
    print(i)

for i in range(-10, 0):
    print(i)

imiona = ["Radek", "Tomek", "Agata", "Marek"]

for p in imiona:
    print(p)

# 0 Radek
for i in range(len(imiona)):
    print(i, imiona[i])

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek

# enumerate() - numeruje kolekcje, zwraca numer i indeks
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Agata')
# (3, 'Marek')
a, b = (0, 'Radek')
print(a, b)
for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Agata
# 3 Marek
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Agata
# 4 Marek
imiona = ["Radek", "Tomek", "Agata", "Marek", "Zenek"]
wiek = [44, 56, 23, 43]

# Radek 44
# for i in range(len(imiona)):
#     print(imiona[i], wiek[i])
#     # IndexError: list index out of range dla róznych list
# Radek 44
# Tomek 56
# Agata 23
# Marek 43

# zip() - łączenie kolekcji
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 56)
# ('Agata', 23)
# ('Marek', 43)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 44
# Tomek 56
# Agata 23
# Marek 43
