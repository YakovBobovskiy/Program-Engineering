with open('input(s_4).txt', 'r') as file:
    bad_words = file.read().split()

text = input()

result = text
for word in bad_words:
    result = result.replace(word, '*' * len(word))
    result = result.replace(word.upper(), '*' * len(word))
    result = result.replace(word.title(), '*' * len(word))

print(result)