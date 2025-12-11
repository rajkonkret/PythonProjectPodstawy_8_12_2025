# funkcja lambda
# skrócony zapis funkcji
# lambda zwraca wynik (return)
# funkcja naonimowa

def odejmij(a, b):
    return a - b


print(odejmij(10, 8))  # 2

odejmij2 = lambda a, b: a - b
print(odejmij2(10, 8))  # 2

oblicz_vat = lambda kwota, vat=23: kwota * (100 + vat) / 100
print(oblicz_vat(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 14, 24, 50, 67, 80, 100, 200, 500]

l1 = []
for i in lista:
    l1.append(i * 2)
print(l1)

print([i * 2 for i in lista])


# [2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))

# map() - wykonuje na kolejnych danch, zadaną funkcję
print(f"Zastosowania map():{list(map(zmien, lista))}")
# Zastosowania map():[2, 4, 28, 48, 100, 134, 160, 200, 400, 1000]

# lambda jako funkcjia anonimowa
print(f"Zastosowania map():{list(map(lambda x: x * 2, lista))}")
print(f"Zastosowania map():{list(map(lambda x: x * 4, lista))}")
print(f"Zastosowania map():{list(map(lambda x: x * 8, lista))}")

# filtrowanie danych
l4 = []
for i in lista:
    if i < 3:
        l4.append(i)
print(l4)  # [1, 2]

# filter() - zwraca elementy spełniajce warunek
print(f"Zastosowannie filter(): {list(filter(lambda x: x < 3, lista))}")
print(f"Zastosowannie filter(): {list(filter(lambda x: x < 50, lista))}")
print(f"Zastosowannie filter(): {list(filter(lambda x: x > 30, lista))}")
print(f"Zastosowannie filter(): {list(filter(lambda x: x > 3 and x < 100, lista))}")
print(f"Zastosowannie filter(): {list(filter(lambda x: 3 < x < 100, lista))}")
# Zastosowannie filter(): [14, 24, 50, 67, 80]
# Zastosowannie filter(): [14, 24, 50, 67, 80]
# Zastosowannie filter(): [1, 2]
# Zastosowannie filter(): [1, 2]
