# słownik - para klucz : wartość
# odpowiednik jsona
# {'user':'Radek', 'wiek':35}
# klucze nie mogą sie powtarzać

# pusty słownik
dictionary = {}
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary_1 = dict()
print(dictionary_1)  # {}
print(type(dictionary_1))  # <class 'dict'>

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 45
print(dictionary)  # {'imie': 'Radek', 'wiek': 45}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 45])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 45)])

# nadpisanie danych
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 45}

# wypisanie wartości ze słownika, po kluczu
print(dictionary['imie'])  # Tomek

dictionary['imie'] = ['Radek', "Tomek", 'Magda']
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 45}
print(dictionary['imie'])  # ['Radek', 'Tomek', 'Magda']
print(dictionary['imie'][0])  # Radek

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

name1 = "GROSS"
name2 = "groẞ"

print(name1.lower() == name2.lower())  # False
print(name1.casefold() == name2.casefold())  # True
#     """ Return a version of the string suitable for caseless comparisons. """

dictionary.update({'data': '12-12-2035'})
print(dictionary)
# {'imie': ['Radek', 'Tomek', 'Magda'], 'wiek': 45, 'data': '12-12-2035'}

dict_small = {'x': 2}
dict_small.update([("y", 2), ("z", 5)])
print(dict_small)  # {'x': 2, 'y': 2, 'z': 5}

# input() - pozwala wprowadzic dane: np.:  z klawiatury
# tekst = input("Podaj imię:")
# print(tekst)
# Podaj imię:Radek
# Radek

# napisac aplikację kalkulator
# input zwraca str
# print(eval("2 + 2"))
# a = float(input("Podaj pierwszą liczbę"))
# b = input("Podaj drugą liczbę")
# print(a + int(b))  # 3.0

# napisac aplikację słownik pol-ang
pol_ang = {"pies": "dog", "kot": "cat", "dach": "roof"}
print(pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia:")
# print(pol_ang[odp])
print(pol_ang.get(odp.strip().casefold(), "Nie ma"))
