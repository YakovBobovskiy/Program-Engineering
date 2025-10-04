from S5_import import triangle_area

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

area = triangle_area(a, b, c)
print(f"Площадь треугольника: {area}")