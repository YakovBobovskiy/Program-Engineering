sentence = input("Введите предложение: ")
print("Длина предложения:", len(sentence))
print("В нижнем регистре:", sentence.lower())

vowels = sum(1 for char in sentence.lower() if char in 'aeiou')
print("Количество гласных:", vowels)

new_sentence = sentence.replace('ugly', 'beauty')
print("После замены:", new_sentence)

print("Начинается с 'The':", sentence.startswith('The'))
print("Заканчивается на 'end':", sentence.endswith('end'))
print()