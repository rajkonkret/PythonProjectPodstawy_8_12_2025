# krotka - tuple - lista tylko do odczytu, niemutowalna
# pozwala efektywniej zarządzać pamięcią
# moze być traktowana jako stała - szczególny przypadek zmiennej

tupla_imiona = "Zenek", "Marek", "Radek", "Ania"
print(type(tupla_imiona))  # <class 'tuple'>
print(tupla_imiona)  # ('Zenek', 'Marek', 'Radek', 'Ania')

tupla_liczby = 43, 55, 33.45, 11, 200
tupla_liczby = (43, 55, 33.45, 11, 200)
print(tupla_liczby)  # (43, 55, 33.45, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

# tupla jednoelementowa
tupla_jeden = (34,)
tupla_jeden = 34,
print(tupla_jeden)  # (34,)
print(type(tupla_jeden))  # <class 'tuple'>

# tupla jest niemutowalna
# tupla_jeden[0] = 123 # TypeError: 'tuple' object does not support item assignment

# usuniecie całej tupli
# del tupla_jeden[0] # to nie zadziałą, TypeError: 'tuple' object doesn't support item deletion
del tupla_jeden
# print(tupla_jeden)  # NameError: name 'tupla_jeden' is not defined


print(len(tupla_imiona))  # długosc 4

tup = 1, 2
print(type(tup))  # <class 'tuple'>

a = tup[0]
b = tup[1]
print(a, b)  # 1 2

a, b = 1, 2
print(a, b)  # 1 2

# rozpakowanie krotki
a, b = tup
print(a, b)  # 1 2

print(tupla_imiona)
print(len(tupla_imiona))  # 4
# ('Zenek', 'Marek', 'Radek', 'Ania')

# * worek na pozostałe dane
*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)
# ['Zenek', 'Marek'] Radek Ania

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)
# Zenek Marek ['Radek', 'Ania']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)
# Zenek ['Marek', 'Radek'] Ania

print(tupla_imiona.count("Radek"))  # 1
print(tupla_imiona.index("Radek"))  # 2

# sorted() - sortowanie
print(sorted(tupla_imiona))  # zwróci liste
# ['Ania', 'Marek', 'Radek', 'Zenek']
print(tupla_imiona)  # nie zostaje zmieniona

lista_tup = list(tupla_imiona)
print(lista_tup)  # ['Zenek', 'Marek', 'Radek', 'Ania']
