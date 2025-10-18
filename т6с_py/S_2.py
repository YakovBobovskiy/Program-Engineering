def remove_first_occurrence(tuple_data, element):
    if element in tuple_data:
        index = tuple_data.index(element)
        return tuple_data[:index] + tuple_data[index+1:]
    return tuple_data

result1 = remove_first_occurrence((1, 2, 3), 1)
result2 = remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)
result3 = remove_first_occurrence((2, 4, 6, 6, 4, 2), 9)

print(result1)
print(result2)
print(result3)