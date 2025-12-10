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
