# napisac aplikacje kalkulator
# while
# menu z opcja
# obsłużyc wyjątki
# wyswietlik ładnie wynik działania
while True:
    print(f"""
          1. Dodaj
          2. Odejmij
          3. Pomnóż
          4. Podziel
          5. Zakończ
          """
          )

    dzialanie = input("Wybierz działanie: ")
    if not dzialanie in ["1", "2", "3", "4"]:
        break
    try:

        x = float(input("Podaj x="))
        y = float(input("Podaj y="))

        if dzialanie == "1":
            # print(f'{x} + {y} = {x + y}')
            print(f"Dodawanie: {x} + {y} = {x + y}")
        elif dzialanie == "2":
            print(f'{x} - {y} = {x - y}')
        elif dzialanie == "3":
            print(f'{x} * {y} = {x * y}')
        elif dzialanie == "4":
            print(f'{x} / {y} = {x / y}')
    except ZeroDivisionError:
        print("Błąd!!!\nDzielenie przez zero!")
    except ValueError:
        print("Błąd!!!\nObsługujemy tylko liczby!")
    except Exception as e:
        print("Błąd działania", e)
    finally:
        "Koniec..."

wyr = "5 *7+12"
print(eval(wyr))

a = 10
b = 30
dict1 = {"dodawanie": a + b}
print(dict1['dodawanie'])
# a = 10
# b = 30
# dict1 = {"dodawanie": a + b}
# print(dict1['dodawanie'])
# 40
