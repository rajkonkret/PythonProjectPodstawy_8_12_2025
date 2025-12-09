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
