# funkcja - wydzielony fragment kodu, który możemy wywołać w dowolny m momencie
# funkcja musi byc najpierw zadeklarowana
# żeby użyc funkcji musimy ją wywołać

a = 6
b = 8


# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # argumenty a i b (obowiązkowe)
    print(a + b)


# symuluje przeciąząnie funkcji liczbą argumentów
def odejmij(a, b, c=0):  # argumenty o wartości domyslnej
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 14

# argumenty pozycyjne
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(10, 89)  # 99

odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4

# przekazywaie po nazwie (keywords)
odejmij(b=9, a=8)  # -1
odejmij(c=9, b=90, a=76)  # -23

# mieszane
odejmij(1, 2, c=78)  # -79
dodaj2(a, b=9)  # 15

# pozycyjne muszą być przed nazwanymi
# odejmij(a=1, 1, 2) # SyntaxError: positional argument follows keyword argument

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + dodaj2(5, 9))
