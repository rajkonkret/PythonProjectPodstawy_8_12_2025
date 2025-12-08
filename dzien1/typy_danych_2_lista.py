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
