# funkcje zwracające wynik
# kończy się słówkiem return

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(kwota, vat=23):
    return kwota * (100 + vat) / 100


print(dodaj(5, 9))  # 14
print(dodaj(6, 9))  # 15

wynik = odejmij(5, 8, 9)
print("Wynik:", wynik)  # Wynik: -12

print(oblicz_vat(1000))
print(oblicz_vat(1000, 15))
print(oblicz_vat(vat=8, kwota=1000))
# 1230.0
# 1150.0
# 1080.0

zm = oblicz_vat(1000)

if zm == 1230:
    print("ok")

print(dodaj(4, 5) + oblicz_vat(1000))  # 1239.0
