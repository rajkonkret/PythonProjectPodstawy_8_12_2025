def connect(**opcje):
    print(opcje)


connect()  # {}
connect(a=100)  # {'a': 100}


def all_args(*args, **kwargs):
    print(args, kwargs)


all_args()  # () {}
all_args(1, 2, 3, 4, 5, 6)  # (1, 2, 3, 4, 5, 6) {}
all_args(1, 2, 3, 4, 5, 6, a=10, b=20)  # (1, 2, 3, 4, 5, 6) {'a': 10, 'b': 20}
all_args(a=10, b=20)  # () {'a': 10, 'b': 20}


def random_radek(*args, k=0):
    print(args, k)


random_radek(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8)
# k musi byc po nazwie bo jest po *args
random_radek(123, k=19)  # (123,) 19
