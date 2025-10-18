def get_office_access(tuple_data, employee_id):
    if employee_id not in tuple_data:
        return ()

    first_index = tuple_data.index(employee_id)

    try:
        second_index = tuple_data.index(employee_id, first_index + 1)
        return tuple_data[first_index:second_index + 1]
    except ValueError:
        return tuple_data[first_index:]

result1 = get_office_access((1, 2, 3), 8)
result2 = get_office_access((1, 8, 3, 4, 8, 8, 9, 2), 8)
result3 = get_office_access((1, 2, 8, 5, 1, 2, 9), 8)

print(result1)
print(result2)
print(result3)