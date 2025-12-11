import json

# '{"name":"John", "age":30, "car":null}'

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

# zapis jako json
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

# beautify
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# sortowanie po kluczach
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

# wczytanie do słownika
with open("nasze_dane.json", "r") as f:
    data = json.load(f)

print(data)
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))
# <class 'dict'>

print(data['name'])  # Radek
# "description":"Zmienna to miejsce w pami\u0119ci komputera, gdzie przechowywana jest warto\u015b\u0107.
# W Pythonie zmienna przypisywana jest do nazwy za pomoc\u0105 operatora `=`.","example":"nazwa = \"Python\"\nwiek = 30\nczy_aktywny = True","id":1,"level":"podstawowy",
# "term":"Co to jest zmienna w Pythonie?"}

# zamiana słownika na json(tekst)
json_tekst = json.dumps(data)
print(json_tekst)  # {"age": 40, "czy_pali": null, "name": "Radek"}
print(type(json_tekst))  # <class 'str'>

# zamiana json na słownik
dict_json = json.loads(json_tekst)
print(type(dict_json))
print(dict_json)  # <class 'dict'>
# {'age': 40, 'czy_pali': None, 'name': 'Radek'}
