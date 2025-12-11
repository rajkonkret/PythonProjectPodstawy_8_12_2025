import chardet

# pip install chardet

# print(chardet)

# "rb" - eczytanie bajtowe - wymaganie biblioteki
with open('test.log', "rb") as file:
    raw_data = file.read()

print(raw_data)
# b'Powitanie2\nDodane\nDodane2\nDodane23\nDod\xc5\x9bane23\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']
print(f"Trafność: {confidence}")
print(f"Kodowanie: {encoding}")

print(raw_data.decode(encoding=encoding))
# Powitanie2
# Dodane
# Dodane2
# Dodane23
# Dodśćźane23
