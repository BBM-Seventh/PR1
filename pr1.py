import math

def calculate_Y(a, b, c, x):
    Y = math.sqrt(x**3 + a*x**2 + b*x + c)
    return Y

a = 2
b = 3
c = 4
x = 5

result = calculate_Y(a, b, c, x)

print(f"A: {a}")
print(f"B: {b}")
print(f"C: {c}")
print(f"X: {x}")
print(f"Результат обчислення Y: {result:.2f}")
