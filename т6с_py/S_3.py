def count_numbers(string):
    dictionary = {}
    for char in string:
        num = int(char)
        dictionary[num] = dictionary.get(num, 0) + 1

    sorted_items = sorted(dictionary.items(), key=lambda x: (-x[1], x[0]))
    top_three = dict(sorted_items[:3])

    return dict(sorted(top_three.items()))

result = count_numbers(input('Введите последовательность цифр: '))
print(result)