import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    return None

nums = one + two + three
min = sorted(nums)[:3]
max = sorted(nums)[-3:]

amin = triangle(*min)
amax = triangle(*max)

print(f"Площадь из минимальных {min}: {amin:.2f}")
print(f"Площадь из максимальных {max}: {amax:.2f}")