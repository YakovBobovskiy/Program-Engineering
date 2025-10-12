grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def fixedGrades(grades):
    return [4 if g == 3 else g for g in grades if g != 2]

print("Исправленные оценки 1:", fixedGrades(grades1))
print("Исправленные оценки 2:", fixedGrades(grades2))
print("Исправленные оценки 3:", fixedGrades(grades3))