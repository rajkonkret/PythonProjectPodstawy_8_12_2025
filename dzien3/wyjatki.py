# wyjątki - błedy wykonania programu
from csv import excel

# print(5 / 0)
# ZeroDivisionError: division by zero

try:
    # print(5/ 0)
    # int("A")
    # print("A" * "23")
    # raise KeyError("Błąd klucza") # rzucenie wyjątku
    value = 90 / 3

except ZeroDivisionError:
    print("Dzielenie przez zero")
except ValueError:
    print("Bład wartości")
except TypeError:
    print("Bład typu")

except Exception as e:
    print("Błąd:", e)
else:  # jak  nie ma błedu
    print(value)
finally:  # wykonuje sie zawsze
    print("Kolejne dane")

print("Program nadal działą")
# print(value)
# Dzielenie przez zero
# Program nadal działą
