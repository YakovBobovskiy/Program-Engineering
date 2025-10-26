with open('input(s_3).txt', 'r') as file:
    text = file.read()

lines = text.split('\n')
line_count = len(lines)

words = text.split()
word_count = len(words)

letter_count = sum(c.isalpha() for c in text)

print("Input file contains:")
print(f"{letter_count} letters")
print(f"{word_count} words")
print(f"{line_count} lines")