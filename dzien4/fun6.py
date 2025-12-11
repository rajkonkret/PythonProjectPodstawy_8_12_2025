# stworzyc funkcję oblizającą średnią (ocen)
def srednia(name=None, *cyfry):  # dowolna ilosc argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma = 0
    sum_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = sum_p / count
    except Exception as e:
        print("Błąd:", e)
    else:
        print(f"Średnia dla ucznia {name}, wynosi: {avg}")
        print(f"Średnia dla ucznia {name}, wynosi: {avg_p}")
    finally:
        print("następny uczeń")


srednia()
srednia(1, 2, 3, 4, 5)
srednia("Radek", 1, 2, 3, 4, 5)
