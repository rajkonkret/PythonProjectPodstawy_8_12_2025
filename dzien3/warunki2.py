# od python 3.10
# match case

lista = []
lng = input("Podaj znany Ci język programowania:")

match lng.strip().casefold():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam jave")
    case _: # odpowiednik elsa
        print("Nie znam tego języka")

print(lista)