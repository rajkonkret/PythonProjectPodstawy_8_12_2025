# kolekcje
from os import killpg

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

a = 1
b = 3
print(f"{a=}, {b=}")  # a=1, b=3
a = b
print(f"{a=}, {b=}")  # a=3, b=3

lista2 = lista  # kopia adresu, referencji
lista_copy = lista.copy()  # kopia eleemntów listy do drugiej listy
print(lista)  # ['Radek', 'Ola', 'Magda', 'Radek']
print(lista2)  # ['Radek', 'Ola', 'Magda', 'Radek']

lista.clear()  # usunięcie wszystkich elementów z listy
print(lista)  # []
print(lista2)  # []
print(lista_copy)  # ['Radek', 'Ola', 'Magda', 'Radek']

# id() - pokazuje referencje
print(id(lista))  # 4309054912
print(id(lista2))  # 4309054912
print(id(lista_copy))  # 4309620480

liczby = [54, 999, 34, 12.34, 567, 999]
print(liczby)  # [54, 999, 34, 12.34, 567, 999]
print(type(liczby))  # <class 'list'>

liczby.sort()  # zmienia oryginał
print(liczby)  # [12.34, 34, 54, 567, 999, 999]

liczby = [54, 999, 34, 12.34, 567, 999, "A"]
print(liczby)  # [54, 999, 34, 12.34, 567, 999, 'A']
print(type(liczby))  # <class 'list'>

# liczby.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

print(lista_copy)
lista_copy.sort()
print(lista_copy)  # ['Magda', 'Ola', 'Radek', 'Radek']

lista_copy.sort(reverse=True)  # sortowanie i odwrócenie
print(lista_copy)  # ['Radek', 'Radek', 'Ola', 'Magda']

lista_copy.reverse()  # tylko odwraca
print(lista_copy)  # ['Magda', 'Ola', 'Radek', 'Radek']

liczby[3] = 666
print(liczby[0:3])  # [54, 999, 34]
print(liczby[-3])  # 567
print(liczby)  # [54, 999, 34, 666, 567, 999, 'A']

# rozpakowanie sekwencji
tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

# tworzenie krotki (tupli) z listy
krotka = tuple(lista_copy)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Magda', 'Ola', 'Radek', 'Radek')
