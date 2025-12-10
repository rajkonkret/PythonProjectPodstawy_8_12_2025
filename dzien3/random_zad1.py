import random

# działąnia na liczbach losowych

"""Return random integer in range [a, b], including both end points.
        """
print(random.randint(1, 100))  # int, 32, od 1 do 100

print(random.randrange(1, 100))  # od 1 do 99
print(random.randrange(5))  # od 0 do 4

print(random.random())  # float, 0.41353692247195595 od 0 do 0.999999
print(random.random() * 9)  # float, 3.901021826497442 od 0 do 8.999999

