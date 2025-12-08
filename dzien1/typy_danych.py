import sys

wiek = 47
rok = 2025
temp = 36.6

print(wiek + rok)  # 2072
print(wiek - rok)  # -1978
print(wiek * rok)  # 95175
print(wiek / rok)  # 0.023209876543209877

print(rok // wiek)  # częśc całkowita z dzielenia, 43
print(rok % wiek)  # reszta z dzielenia, modulo

print(wiek ** rok)  # potęgowanie

print(len(str(wiek ** rok)))  # 3386
# print(len(str(wiek ** rok ** 2))) # 3386
# Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 6 * 43 + 4 / 2 + 4 / 2)  # -200.0
print(54 - 6 * 43 + (4 / 2 + 4) / 2)  # -201.0

# bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# For example, in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

# decimal() - obejcie problemu zaokrąglenia

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
# min=2.2250738585072014e-308, min_exp=-1021,
# min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# typ logiczny
# prawda, fałsz
# True, False
# 1, 0

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True
print(bool("Radek"))  # True

print(bool(0))  # False
print(bool(""))  # False

print(bool(None))  # False, wartosc nieokreślona, brak danych, nie wiem, odpowiednik null

print(40 * "-")

# operacje logiczne
# and - i
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or - lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

a = 6
b = 8

print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 6 > 8 = False#    Porównanie 6 > 8 = False
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 6 < 8 = True#     Porównanie 6 < 8 = True
print(f"Porównanie {a} <= {b} = {a <= b}")  # Porównanie 6 <= 8 = True#  Porównanie 6 <= 8 = True
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 6 >= 8 = False# Porównanie 6 >= 8 = False
print(f"porównanie { a >= b = }")  # porównanie  a >= b = False
#                    "a >= b = "
print(f"Porównanie {a} == {b} = {a == b}")  # == czy równe? Porównanie 6 == 8 = False
print(f"Porównanie {a} != {b} = {a != b}")  # != czy różne? Porównanie 6 != 8 = True
