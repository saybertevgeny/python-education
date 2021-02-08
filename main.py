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
print(long_string.split())   # ['This', 'is', 'long', 'string'] по умолчанию разделитель пробел
print(long_string.split('s'))  # ['Thi', ' i', ' long ', 'tring']

