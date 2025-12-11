# stworzyc funkcję kantor
# ma miec dwie funkcje wewnetrzne: usd, eur
# w zalezności od parametrów ma zwrócic jedną lub drugą funkcję (if)
# przekazanie argumentu (kwota) do funkcji eur i usd

def kantor(waluta):
    def usd(kwota=0):
        print(f"wymieniam {kwota} usd na pln={kwota * 3.61}")

    def eur(kwota=0):
        print(f"wymieniam {kwota} eur na pln={kwota * 4.23}")

    if waluta == "usd":
        return usd
    else:
        return eur


kantor_usd = kantor("usd")
kantor_usd()
kantor_usd(1000)
kantor_usd(500)
kantor_usd(444)
# wymieniam 0 usd na pln=0.0
# wymieniam 1000 usd na pln=3610.0
# wymieniam 500 usd na pln=1805.0
# wymieniam 444 usd na pln=1602.84

kantor_eur = kantor("eur")
kantor_eur(1000)
kantor_eur(150)

kantor_usd(567)
# ymieniam 1000 eur na pln=4230.0
# wymieniam 150 eur na pln=634.5000000000001
# wymieniam 567 usd na pln=2046.87
