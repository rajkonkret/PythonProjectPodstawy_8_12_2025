import random

# działąnia na liczbach losowych

"""Return random integer in range [a, b], including both end points.
        """
print(random.randint(1, 100))  # int, 32, od 1 do 100

print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # float, 0.41353692247195595 od 0 do 0.999999
print(random.random() * 9)  # float, 3.901021826497442 od 0 do 8.999999

lista = [67, 45, 32, 68, 90, 42, 69]
print(lista[random.randrange(len(lista))])  # 69

print(random.choice(lista))  # 67

lista_kule = list(range(1, 50))
# print(lista_kule)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # [6, 5, 44, 43, 15, 5], z powtórzeniami
print(random.sample(lista_kule, k=6))  # [14, 42, 4, 40, 30, 49], bez powtórzen
