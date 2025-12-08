# https://peps.python.org/pep-0008/
# snake_case
import sys

# ctrl alt l - formatowanie PEP8
print()  # wydrukuj/wypisz

print("Radek")
print("Radek")
print("Radek")
print("Radek")
print("Radek")
# ctrl d  - powielanie linii
print('Radek')

# print('Radek")
#   File "/Users/radoslawjaniak/PycharmProjects/PythonProjectPodstawy_8_12_2025/dzien1/pierwszy.py", line 15
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 15)
#
# Process finished with exit code 1
# ctrl / - komentarz

print("Radek\"Radek\"")  # Radek"Radek", \ - znak ucieczki

# type() - sprawdzanie typów danych
print(type("Radek"))  # <class 'str'>, dane tekstowe

print("39" + "39")  # 3939, łączenie stringów

print(39 + 39)  # 78
print(type(39))  # <class 'int'>, liczby cąlkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4,
# default_max_str_digits=4300, str_digits_check_threshold=640)

# print(39 + "39")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# rzutowanie - zamiana na typ liczbowy
print(int("39"))
print(39 + int("39"))  # 78

print(str(39))  # rzurtowanie na string
print("Kowalski" + str(1))  # Kowalski1

print(5 * "4")  # 44444
print(35 * "168")
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168

# zmienna - pudełko na dane

# typowanie dynamiczne
name = "Radek"
print(type(name))  # <class 'str'>
print(name)  # Radek

name = 90
print(name)  # 90
print(type(name))  # <class 'int'>

# podpowiedzi typów
name: str = "Raadek"
print(name)

name = 90
print(name)
# mypy - sprawdzanie uzycia typów
# pip - menadżer pakietów
#  pip install mypy
# cd dzien1
# cd .. - poziom wyzej
# (.venv) radoslawjaniak@MacBook-Air-radosaw-2 dzien1 % mypy pierwszy.py
# pierwszy.py:59: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# pierwszy.py:64: error: Name "name" already defined on line 55  [no-redef]
# pierwszy.py:67: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) radoslawjaniak@MacBook-Air-radosaw-2 dzien1 %
