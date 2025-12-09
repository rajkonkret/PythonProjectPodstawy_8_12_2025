# kolekcje

# lista - przechowuje dowolną ilość dnych, różnego typu
# zachowuje kolejności

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodawanie lementów na końcu listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")
lista.append("Magda")
lista.append("Paulina")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Magda', 'Paulina']
#    0         1         2       3        4         5
print(len(lista))  # 6

print(lista[2])  # Zenek
print(lista[4])  # Magda

# print(lista[10]) # IndexError: list index out of range

# ostatni element listy
print(lista[5])  # Paulina
print(lista[len(lista) - 1])  # Paulina
print(lista[-1])  # Paulina

# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Magda', 'Paulina']
#    0         1         2       3        4         5
#   -6          -5       -4      -3       -2       -1

print(lista[-3])  # Marek

# slicowanie - fragment listy
print(lista[0:3])  # 012, ['Radek', 'Tomek', 'Zenek']
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']

print(lista[2:])  # ['Zenek', 'Marek', 'Magda', 'Paulina'], z ostatnim włącznie
print(lista[2:5])  # ['Zenek', 'Marek', 'Magda'] bez ostatniego

print(lista[2:30])  # ['Zenek', 'Marek', 'Magda', 'Paulina']
print(lista[12:24])

print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Magda', 'Paulina']

# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Magda', 'Paulina']
#    0         1         2       3        4         5
#   -6          -5       -4      -3       -2       -1
print(lista[-2:0])  # [4:0], []
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek', 'Marek'] [0:4]

# range() - generuje liczby z zakresu
lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(lista_15[0:15:2])  # [start:stop:krok], [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[::3])  # [0, 3, 6, 9, 12]

print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14] (start, stop, krok)

# wyswietli liste w odwrotnej kolejności
print(lista[::-1])
# ['Paulina', 'Magda', 'Marek', 'Zenek', 'Tomek', 'Radek']

# nadpiasnie elementu w liscie, na wskazanym indeksie
lista[3] = "Asia"
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Asia', 'Magda', 'Paulina']

lista.insert(1, "Ola")
print(lista)
# ['Radek', 'Ola', 'Tomek', 'Zenek', 'Asia', 'Magda', 'Paulina']

lista_nowa = []
lista_nowa.insert(1, "Drek")
print(lista_nowa)  # ['Drek']

# usuniecie elementu z listy po elemencie, pierwsza z lewej
lista.remove("Tomek")
print(lista)
# ['Radek', 'Ola', 'Zenek', 'Asia', 'Magda', 'Paulina']

# dodac Asia, i usunąć Asia
lista.append("Asia")
print(lista)
# ['Radek', 'Ola', 'Zenek', 'Asia', 'Magda', 'Paulina', 'Asia']
lista.remove("Asia")
print(lista)
# ['Radek', 'Ola', 'Zenek', 'Magda', 'Paulina', 'Asia']

# usunięcie po indeksie
# pop() - zwraca usunięty element
print(lista.pop(2))  # Zenek
zmienna = lista.pop(-1)
print("Usunięto:", zmienna)  # Usunięto: Asia
print(lista)  # ['Radek', 'Ola', 'Magda', 'Paulina']

print(lista.pop())  # Paulina

lista.append("Radek")
print(lista)
# ['Radek', 'Ola', 'Magda', 'Radek']

# sprawdzzenie indeksu dla elementu, pierwszy z lewej
print(lista.index("Radek"))  # indeks 0


