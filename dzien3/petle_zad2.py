dictionary = {'imie': "Radek", "nazwisko": "Kowalski"}

# wypisze klucze
for i in dictionary:
    print(i)

for i in dictionary.keys():
    print(i)

# wypisanie wartości
for v in dictionary.values():
    print(v)

# wypisanie pary
for i in dictionary.items():
    print(i)

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
for k, v in dictionary.items():
    print(k, v, sep="<==>")
# imie<==>Radek
# nazwisko<==>Kowalski
for k, v in dictionary.items():
    print(k, v, end=" | ")
# imie Radek | nazwisko Kowalski |
print("Radek")
# imie Radek | nazwisko Kowalski | Radek
print("Dalej")
# Dalej

pol_ang = {"pies": "dog", "kot": "cat", "dach": "roof"}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}

# dict comrehensions
print({v: k for k, v in pol_ang.items()})
# {'dog': 'pies', 'cat': 'kot', 'roof': 'dach'}
