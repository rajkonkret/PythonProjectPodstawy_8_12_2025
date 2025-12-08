user = "Tomek"  # str
wiek = 39  # int
wersja = 3.90001
print(type(wersja))  # zmiennoprzecinkowa, <class 'float'>
print(wersja)  # 3.90001

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# %s - str
# %d - digit

# TypeError: %d format: a real number is required, not str
# sprawdza typy
# print("Witaj %d, masz teraz %s lat." % (user, wiek))

# f - string
print(f"Witaj {user}, masz teraz {wiek} lat.")
# Witaj Tomek, masz teraz 39 lat.
# %i - int
# %f - float

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %.2f" % 3.9)  # Używamy wersji pythona 3.90
print("Używamy wersji pythona %.1f" % 3.9)  # Używamy wersji pythona 3.9
print("Używamy wersji pythona %.0f" % 3.9)  # Używamy wersji pythona 4 zaokrągla
print("Używamy wersji pythona %.f" % 3.9)  # Używamy wersji pythona 4 zaokrągla

x = 3.8769
print(x)  # 3.8769
y = round(x)
print(y)  # 4

z = round(x, 2)
print(z)  # 3.88
print(type(z))  # <class 'float'>

print(f"Używam wersji pythona {wersja}")  # Używam wersji pythona 3.90001
print(f"Używam wersji pythona {wersja:.2f}")  # Używam wersji pythona 3.90
print(f"Używam wersji pythona {wersja:.1f}")  # Używam wersji pythona 3.9
print(f"Używam wersji pythona {wersja:.0f}")  # Używam wersji pythona 4

print(f'{user:<10}')  # "Tomek     " wyrównaj do lewej
print(f'{user:>15}')  # "          Tomek"
print(f'{user:^20}')  # "       Tomek        "
print(f'{user:.^20}')  # ".......Tomek........"
