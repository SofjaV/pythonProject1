"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""
import datetime

# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

print(datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p'))

print(datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d'))

print(datetime.datetime.strptime(sample3, '%A, %B %d, %Y'))

print(datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S'))


# Write a program to print yesterdays, today and tomorrow dates
today = datetime.date.today()
tdelta = datetime.timedelta(days=1)
yesterday = today - tdelta
tomorrow = today + tdelta
print(yesterday)
print(today)
print(tomorrow)


# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
day_convert = datetime.date.fromtimestamp(some_day)
print(datetime.date.strftime(day_convert, '%d.%m.%Y'))


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)

input = 1234050960

def timestamp():
    global input
    input_conv = datetime.datetime.fromtimestamp(input)
    tdelta2 = datetime.timedelta(weeks=2)
    output_conv = input_conv - tdelta2
    output = output_conv.timestamp()
    print (output)

timestamp()



