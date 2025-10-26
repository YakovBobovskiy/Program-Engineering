import string

with open('input(s_5).txt', 'r') as file:
    text = file.read()

if text.strip():
    words = text.split()
    word_count = len(words)

    char_count = len(text)
    letter_count = sum(c.isalpha() for c in text)
    digit_count = sum(c.isdigit() for c in text)
    space_count = sum(c.isspace() for c in text)

    print(f"Текст: {text}")
    print(f"Слов: {word_count}")
    print(f"Символов: {char_count}")
    print(f"Букв: {letter_count}")
    print(f"Цифр: {digit_count}")
    print(f"Пробелов: {space_count}")

    if words:
        longest_word = max(words, key=len)
        print(f"Самое длинное слово: '{longest_word}' ({len(longest_word)} букв)")
    else:
        print("В тексте нет слов")
else:
    print("Файл пустой")