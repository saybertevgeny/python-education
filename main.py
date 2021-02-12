# Tuple - кортеж, тот же List только не изменяемый
tuple_1 = (1, 2, 3)
tuple_2 = ("one", 'hello')
tuple_3 = (3, 2.3, 'three')
print(tuple_1)  # (1, 2, 3)
print(tuple_2)  # ('one', 'hello')
print(tuple_3)  # (3, 2.3, 'three')

tuple_4 = 1, 2, 3
print(tuple_4)  # (1, 2, 3)
print(type(tuple_4))  # <class 'tuple'>

print(tuple_1[1])  # 2 , как в списках
# tuple_1[1] = 3 ошибка

# распоковка элементов
x = y = z = 12
print(x, y, z)  # 12 12 12
x, y, z = tuple_1
print(x, y, z)  # 1 2 3
x, y, z = 12, 13, 14
print(x, y, z)  # 12 13 14

person_tuple = ('John', 'Smith', 1986)  # неизменямый
first_name, last_name, year_of_birth = person_tuple
print(first_name, last_name, year_of_birth)  # first_name, last_name, year_of_birth

t1 = 1, 2, 3, 4, 5, 1, 7, 9
print(t1.count(1))  # 2 два раза встречается еденица
print(t1.count(5))  # 1 один раз встречается пятерка

greetings_tuple = ('hi', 'hello', 'hi', 'hey')
print(greetings_tuple.count('hi'))  # 2
print(greetings_tuple.count('hola'))  # 0

print(t1.index(5)) # 4
print(greetings_tuple.index('hey')) # 3
print(greetings_tuple.index('hi')) # 0 первый попавшийся
#print(greetings_tuple.index('hola')) ошибка
