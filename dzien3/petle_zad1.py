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
    print(p) # kolejne elementy listy
# Ala
# Tomek
# Zenek
# Basia

