def process_student_grades(student_data):
    grades_dict = {}
    for name, grades in student_data:
        grades_dict[name] = tuple(grades)

    best_student = max(grades_dict.items(), key=lambda x: sum(x[1]))
    worst_student = min(grades_dict.items(), key=lambda x: sum(x[1]))

    return best_student, worst_student

test1 = [('Анна', [5, 4, 5]), ('Иван', [3, 4, 3]), ('Мария', [5, 5, 5])]
test2 = [('Александр', [2, 3, 4]), ('Ольга', [5, 4, 5]), ('Михаил', [4, 4, 4])]
test3 = [('Илья', [3, 3, 3]), ('Екатерина', [4, 4, 4]), ('Сергей', [5, 4, 5])]

print(process_student_grades(test1))
print(process_student_grades(test2))
print(process_student_grades(test3))