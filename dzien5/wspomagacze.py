# github copilot, tabnine, jetbrain ai
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    return a ** b

# napisz funkcę obliczającą s®ednią ocen
def average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)
# napisz funkcję sprawdzającą czy liczba jest parzysta
def is_even(number):
    return number % 2 == 0
# napisz funkcję zwracającą największą liczbę z listy
def max_in_list(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
# napisz funkcję zwracającą najmniejszą liczbę z listy
def min_in_list(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num
# napisz funkcję zwracającą ilość wystąpień elementu w liście
def count_occurrences(elements, target):
    count = 0
    for element in elements:
        if element == target:
            count += 1

    return count

# napisz funkcję zwracającą listę unikalnych elementów z listy
def unique_elements(elements):
    unique = []
    for element in elements:
        if element not in unique:
            unique.append(element)
    return unique

# napisz funkcję sprawdzającą czy słowo jest palindromem
def is_palindrome(word):
    return word == word[::-1]
# napisz funkcję zwracającą factorial liczby

