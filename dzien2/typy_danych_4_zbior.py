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
print(zbior_copy)
print(id(zbior_copy))  # 4300362624
print(id(zbior))  # 4300363744
