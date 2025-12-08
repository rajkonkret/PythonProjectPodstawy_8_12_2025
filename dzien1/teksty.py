tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))

# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
#         """ Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)  # nie zmienia oryginału
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE

print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie

# Witaj Świecie
# 01234567890..
print(tekst[2])  # indeksowanie od 0, t

print(tekst.index("Ś"))  # indeks numer: 6

print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("i", 0, 4))
print(tekst.count("j", 0, 4))  # 0 razy, z prawej zbiór otwarty

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usuniecie białych znków (wiodących, kończących spacji)

print(tekst.removeprefix("Witaj").strip())  # "Świecie"

encode_s = tekst.encode("utf-8")
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>, dane bajtowe
print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
print(len(imie))  # dlugość 5

# f - string format - wstrzykiwanie wartości zmiennych do tekstu
tekst_format = f'Mam na imię {imie}'
print(tekst_format)  # Mam na imię Radek

tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# \t tab
# \n - nowa linia
# \b backspace
# "	Mam na imię Radek
#  i lubię pythona"

starszy = 'Witaj %s!'  # %s - string
print(starszy % imie)  # Witaj Radek!

print("Witaj {}".format("Radek"))  # Witaj Radek

print("Witaj", imie)  # Witaj Radek

print("""
Teskt
    wielolinijkowy""")
# "Teskt
#     wielolinijkowy"

# dokumentacja
"""Komentarz 
    wielolinijkowy"""
