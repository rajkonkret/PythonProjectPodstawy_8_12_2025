# zbior (set) - przechppwuje unikalne wartosci (brak duplikatów)
# # nie zachowuje kolejnoci przy dodawniu elementów
# nie posiadają indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11, 44]
zbior = set(lista)  # zamiana na zbiór

print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbior
zb2 = set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodawanie elemntow do zbior
zb2.add(33)
zb2.add(33)
zb2.add(33)
zb2.add(18)
zb2.add(18)
zb2.add(24)
zb2.add(24)
zb2.add(24)
zb2.add(25)
print(zb2)
# {24, 33, 18, 25}

zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(24)
zbior.add(24)
zbior.add(24)
zbior.add(25)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24, 25}

# usuniecie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24, 25}

# pop() - usunie i zwróci pierwszy elemnt
print(zbior.pop())  # 33

zmienna = zbior.pop()
print(f"Zmienna: {zmienna}")  # Zmienna: 66

zbior_copy = zbior.copy()
print(zbior_copy)  # {18, 22, 24, 777, 11, 44, 25}
print(id(zbior_copy))  # 4300362624
print(id(zbior))  # 4300363744

print(zbior)  # {777, 11, 44, 18, 22, 24, 25}
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów - zwraa nowy zbiór
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}

# część wspólna - tworzy nowy zbiór
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# różnica zbiorów
print(zbior - zbior_2)
print(zbior.difference(zbior_2))
print(zbior_2.difference(zbior))

# łaczy zbiory, zmieia bazowy!!!
zbior.update(zbior_2)
print(zbior)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62)

lista = list(zbior)
print(lista)  # [777, 11, 44, 12.34, 18, 52, 22, 24, 25, 667, 62]

# sprawdzenie czy element istnieje w kolekcji
print(667 in zbior)  # True
print(667 in krotka)  # True
print(667 in lista)  # True
print(779 in lista)  # False
