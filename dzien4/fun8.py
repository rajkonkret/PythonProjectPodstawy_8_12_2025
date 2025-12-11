def all_params(a, b, /, c=42, d=256):
    print(f"{a=}, {b=}")
    print(f"{c=}, {d=}")




def all_params2(name, b, /, c=42, *args, d=67, **kwargs):
    print(f"{name=}")
    print(f"{b=}")
    print(f"{c=}")
    print(f"{d=}")
    print(f"{args=}")
    print(f"{kwargs=}")

if __name__ == '__main__':

    all_params(1, 2)
    all_params(1, 2, 3, 4)


    # TypeError: all_params() got some
    # positional-only arguments passed as keyword arguments: 'a, b'
    # all_params(a=1, b=2)
    # a=1, b=2
    # c=42, d=256
    # / rozdiela mozliwosc uzycia argumentow
    # po lewej stronie tylko po pozycji
    all_params2(1, 2)
    all_params2("Raeedk", 2, 4)
    all_params2("Raeedk", 2, c=4)
    all_params2("Raeedk", 2, 4, 1, 2, 3, 4, 5, 6, 7, 8)
    all_params2("Raeedk", 2, 4, 1, 2, 3, 4, 5, 6, 7, 8, d=90)
    all_params2("Raeedk", 2, 4, 1, 2, 3, 4, 5, 6, 7, 8, d=90, temat="Topic")
    all_params2("Raeedk", 2, 4, 1, 2, 3, 4, 5, 6, 7, 8, d=90, temat="Topic", b=1)
