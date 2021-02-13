# range(начальное значение =0,конечное значение, интервал = 1
for x in range(3, 11):
    print(x)  # 3 4 5 ... 10

for x in range(3, 11, 5):
    print(x)  # 3 8

print(range(5))  # range(0, 5)
print(list(range(5)))  # [0, 1, 2, 3, 4]

# letter_index = 0
my_string = 'asdasdasda'
# for letter in my_string:
#     print(letter + " is at index " + str(letter_index)) # a is at index 0
#     letter_index += 1
#

for item in enumerate(my_string):
    print(item)  # ... (8, 'd') ... - Tuple

for index, item in enumerate(my_string):
    print(index, item)  # 0 a ....

print('a' in 'Jack')  # True
print('x' in 'Jack')  # False
print(str(1) in 'Jack')  # False
# print(1 in 'Jack')  # Ошибка

letter_list = ['a', 'b', 'c']
print('a' in letter_list)  # True
print(1 in letter_list)  # False

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
print(1 in dict_1)  # True по умолчанию ключи получаем
print(1 in dict_1.keys())  # True
print(1 in dict_1.values())  # False
print('c' in dict_1.values())  # True

print(min(1, 2, 3, 4, 5, 6))  # 1
print(max(1, 2, 3, 4, 5, 6))  # 6

my_list = [1, 2, 3, 4, 5, 6]
print(min(my_list))  # 1
print(max(my_list))  # 6
print(max('Hello'))  # o
for letter in 'Hello':
    print(ord(letter))  # 72 101 108 108 111

from random import shuffle

shuffle(my_list)
print(my_list)  # [1, 2, 6, 3, 4, 5] В случайном порядке

from random import randint

print(randint(1, 10))  # 4 случайное число в диапозоне от 1 до 10
