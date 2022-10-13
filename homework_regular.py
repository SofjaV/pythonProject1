import re

# 1. Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.
#     HASH цвета используют значения от 0 до 15, где 0-9 цифры от нуля до 9, 10-15 буквы от A-F.
with open('colors.txt', 'r') as file:
    data = file.read()
pattern = re.compile(r'#[0-9A-F]{6}')
matches = pattern.finditer(data)
for match in matches:
    print(match)

# 2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +. (Примеры выражений “2*9-6*5” или (3+5)-9*4)
number = '''“2*9-6*5”
(3+5)-9*4
'''

pattern = re.compile(r'\d([^+]|\n)')
matches = pattern.finditer(number)
for match in matches:
    print(match)


# 3. Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00.
# Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время.

time = '''Завтрак в 09:00.
37:98
25:63'''

with open('time.txt', 'r') as file:
    data = file.read()
pattern = re.compile(r'\b([01][0-9]|2[0-4]):([0-5][0-9]\b)')
matches = pattern.finditer(time)
for match in matches:
    print(match)


# 4. Написать программу котороая будет выбирать из файла people.txt:
# 	1) Все имена и фамилии
#   2) Все адреса
with open('people.txt', 'r') as file:
    data = file.read()
pattern = re.compile(r'([A-Z][a-z]+ [A-Z][a-z]+(-[A-Z]|[a-z]+)[a-z]+)|'
                     r'[0-9]{3} .+')
matches = pattern.finditer(data)
for match in matches:
    print(match)



# 5. Написать регулярное выражение для проверки строки, задача определить состоит ли строка из символов a-z, A-Z, 0-9.
symbols = '''KDJSLJGP{EjkjkjPW{APA<NMNBGJ_GJGJJ
GEOWPWA:ADQ090909QQQQ
AASDV:KSg
kgklkoorl'''
pattern = re.compile(r'[A-Za-z0-9]+')
matches = pattern.finditer(symbols)
for match in matches:
    print(True)
else:
    pass



# 6. Написать регулярное выражение для определения эстонского личного кода (isikukood)
id = '''
38803160272
45509042922
48529344751
48112934475
'''
pattern = re.compile(r'\b[1-8][0-9][0-9]([0][1-9]|[1][0-2])([0][1-9]|[1][0-9]|[2][0-9]|[3][01])\d\d\d\d')
matches = pattern.finditer(id)
for match in matches:
    print(match)
