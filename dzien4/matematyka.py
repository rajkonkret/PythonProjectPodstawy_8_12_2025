import math

print(math.pi)  # 3.141592653589793

print(math.sqrt(25))  # 5.0

angle_degree = 30
angle_radias = math.radians(angle_degree)
print(angle_radias)
sin_value = math.sin(angle_radias)
print(f"sin({angle_degree}) = {sin_value}")
# sin(30) = 0.49999999999999994

angles = [0, 30, 45, 60, 90]

sin_values = [math.sin(math.radians(a)) for a in angles]

for a, s in zip(angles, sin_values):
    print(f'sin({a}) = {s:.2f}')
# sin(0) = 0.00
# sin(30) = 0.50
# sin(45) = 0.71
# sin(60) = 0.87
# sin(90) = 1.00

imiona = ["Radek", "Tomek", "Agata", "Marek", "Zenek"]
wiek = [44, 56, 23, 43]
