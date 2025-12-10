# while - pętla sterowana warunkiem

# while True:
#     print("komunikat")

licznik = 0
while True:
    licznik += 1
    print("komunikat2!!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)
licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")

# password = input("Podaj hasło:")
# while password != "secret":  # != różne
#     password = input("Podaj ponownie:")

# Podaj hasło:asasa
# Podaj ponownie:asdeda
# Podaj ponownie:asdasdas
# Podaj ponownie:zzxcvcz
# Podaj ponownie:secret

lista = []
lista_int = []

while True:
    wej = input("Podaj liczbę: ")
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
