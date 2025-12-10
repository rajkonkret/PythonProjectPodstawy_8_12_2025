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
