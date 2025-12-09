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
