from collections import Counter

prepositions = {'и', 'не', '–', 'в', 'на', 'с', 'по', 'у', 'о', 'от', 'до', 'за', 'из', 'к', 'но', 'а', 'или', 'то', 'же', 'бы', 'ли', 'как', 'что', 'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}

with open('article.txt', 'r', encoding='utf-8') as file:
    text = file.read()

all_words = text.split()
filtered_words = [word for word in all_words if word.lower() not in prepositions]

word_count = len(all_words)
most_common = Counter(filtered_words).most_common(1)[0]

print(f"Количество слов: {word_count}")
print(f"Наиболее встречающееся слово: '{most_common[0]}' ({most_common[1]})")