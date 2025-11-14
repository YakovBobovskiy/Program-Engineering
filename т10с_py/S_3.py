def add_two(x):
    try:
        x = float(x)
        return 2 + x
    except (ValueError, TypeError):
        print("Неподходящий тип данных")

print(add_two(5))
print(add_two("10"))
print(add_two("abc"))