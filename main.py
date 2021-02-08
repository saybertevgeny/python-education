greeting = 'Hello world!'
greeting_len = len(greeting)
print(greeting_len)

# Indexing
print(greeting[0])
print(greeting[6])

print(greeting[-1])
# print(greeting[12]) У меня возникает ошибка
print(greeting[-4])

# Slicing
print(greeting[2:5])  # llo т.е. конец не включается
print(greeting[6:11])  # world
print(greeting[-5:-2])  # orl
print(greeting[2:])  # llo world! т.е. вырезание до конца
print(greeting[:5])  # Hello т.е. вырезание с начала строки
print(greeting[:])  # вся строка

print(greeting[::2])  # Hlowrd т.е. перескок через одну букву
print(greeting[::1])  # Hello world!
print(greeting[::3])  # Hlwlт.е. перескок через дву буквы
print(greeting[1:6:3])  # eo т.е. перескок через дву буквы с 1 по 6(не включая)

print(greeting[::-1])  # !dlrow olleH вывести наоборот, начинаем с 0 до конца, и -1 в третьем параметре это с конца

# Свойства и методы строк

# Imutable
first_name = 'Jake'
print(first_name[2])
# first_name[2] = "n" Ошибка, строки неизменяемы
# print(first_name)

first_two_letters = first_name[:2]
print(first_two_letters)  # Ja
last_letter = first_name[-1:]
print(last_letter)  # e

# Concatenable
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)  # Jane

greeting = 'Hello!'
greeting = greeting + ' Python!'
print(greeting)  # Hello! Python! Так можно, т.к. строку частично не меняем

# Multiplication
yummy = 'Yum '
print(yummy * 2)  # Yum Yum

print(yummy.upper())  # YUM
print(yummy.lower())  # yum в этих двух методах создаются !новые! строки

long_string = 'This is long string'
print(long_string.split())  # ['This', 'is', 'long', 'string'] по умолчанию разделитель пробел
print(long_string.split('s'))  # ['Thi', ' i', ' long ', 'tring']

# Форматирование строк
age = 23
# print("Jack is" + age + "years old")  # Ошибка, можно конкатенировать только строки со строками
print("Jack is " + str(age) + " years old")  # Jack is 23 years old
print("Jack is " + str(23) + " years old")  # Jack is 23 years old

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old'.format(name, age)  # My name is Jack. I'm 23 years old
print(name_and_age)

name_and_age = 'My name is {}. I\'m {} years old'.format(name, age)
print(name_and_age)  # My name is Jack. I'm 23 years old

week_days = 'There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}.'.format("Monday", "Tuesday", "Wednesday",
                                                                             "Thursday", "Friday", "Saturday", "Sunday")
print(week_days)  # There are 7 days in a week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

week_days = 'There are 7 days in a week: {6}, {0}, {1}, {2}, {3}, {4}, {5}.'.format("Monday", "Tuesday", "Wednesday",
                                                                                    "Thursday", "Friday", "Saturday",
                                                                                    "Sunday")
print(week_days)  # There are 7 days in a week: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday.

week_days = 'There are 7 days in a week: {su}, {mo}, {tu}, {we}, {th}, {fr}, {sa}.'.format(mo="Monday",
                                                                                           tu="Tuesday",
                                                                                           we="Wednesday",
                                                                                           th="Thursday",
                                                                                           fr="Friday",
                                                                                           sa="Saturday",
                                                                                           su="Sunday")
print(week_days)  # There are 7 days in a week: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday.

float_result = 1000 / 7
print(float_result)  # 142.85714285714286
print("The result of division is {0}".format(float_result))  # The result of division is 142.85714285714286
print("The result of division is {0:1.3f}".format(
    float_result))  # The result of division is 142.857, где 1 количество символов для обрезки
print("The result of division is {0:10.3f}".format(
    float_result))  # The result of division is    142.857, как видно появился пробел

print('''
    {0} {1} {2}  
    {3} {4} {5}
    {6} {7} {8}
'''.format(1.45778, 345.231231, 31.1231,  # 1.45778 345.231231 31.1231
           11.121, 1212.1, 5621.1,  # 11.121 1212.1 5621.1
           1.45, 11.2132131, 3))  # 1.45 11.2132131 3

print('''
    {0:10.2f} {1:10.2f} {2:10.2f}  
    {3:10.2f} {4:10.2f} {5:10.2f}
    {6:10.2f} {7:10.2f} {8:10.2f}
'''.format(1.45778, 345.231231, 31.1231,  # 1.46     345.23      31.12
           11.121, 1212.1, 5621.1,  # 11.12    1212.10    5621.10   т.е. для формитирования
           1.45, 11.2132131, 3))  # 1.45      11.21       3.00

name = 'Jack'
age = 23
name_and_age = f'My name is {name}. I\'m {age} years old'
print(name_and_age)  # My name is Jack. I'm 23 years old т.е. сразу можно указывать переменные

print('My name is %s. I\'m %d years old' % (name, age))  # My name is Jack. I'm 23 years old
print('My name is %s. %s %d years old' % (name, "I'm", age))  # My name is Jack. I'm 23 years old !DEPRECATED!
