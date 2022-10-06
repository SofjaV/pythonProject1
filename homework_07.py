# Написать программу которая открывает текстовый файл и считает следующее:
# 1. Общее кол-во слов
# 2. Кол-во уникальных (разных)
#
# Не влияет на уникальность:
# Заглавные и прописные буквы
# Знаки препинания: ',' '.' '!' '?'
#
# Сохраняет кол-ва в отдельный файл.
# Выписывает все уникальные слова в алфавитном порядке (по одному слову в строке).


with open(f'tri.txt', 'r', encoding='utf-8') as file:
    data = file.read()

data = data.lower().replace('\n', ' ').replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').replace('"', ' ').replace(' - ', ' ').replace(':', ' ').replace(';', ' ').replace('*', ' ').replace(')', ' ').replace('(', ' ')
words = data.split()

words_unique = []
for word in words:
    if word not in words_unique:
        words_unique.append(word)
words_unique.sort()
print('\n'.join(words_unique))

with open(f'new_file.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(str((len(words_unique))))
    new_file.write('\n')
    new_file.write(str((len(words))))
    new_file.write('\n')
    new_file.write(str(('\n'.join(words_unique))))
