# funkcja wewnętrzna, zagnieżddzona

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy adres funckji


fun1()
print(fun1())  # <function fun1.<locals>.fun2 at 0x100611a80>
print(type(fun1()))  # <class 'function'>
xfun = fun1()
xfun()  # To jest fun2
# To jest fun1
# To jest fun2
