a = float(input("Enter coefficients of the quadratic equation: \na = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0 and b != 0:
    x = -c / b
    print(f"Result: x = {x}")
elif a != 0:
    d = b ** 2 - 4 * a * c
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f"Result: x1 = {x1}; x2 = {x2}")
else:
    print("Result: x = 0")
