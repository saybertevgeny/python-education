number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in number_list:
    if number % 2 == 0:
        print(number)  # 2 4 6 8 10
    else:
        print('Hey')  # Hey

greeting = 'Hello Python'
for letter in greeting:
    if letter == 'o':
        print(letter)

tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for item in tuple_list:
    print(item)  # ('a', 'b') ...

for letter_1, letter_2 in tuple_list:
    print(letter_1, letter_2)  # a b ...

dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# keys
for item in dictionary:
    print(item)  # key1 key2 ...
    # print(dictionary.get(item))  # value1 ....
# key-value
for item in dictionary.items():
    print(item)  # ('key1', 'value1') ....
# value
for item in dictionary.values():
    print(item)  # value1 ....

print(range(5))  # range(0, 5)
test = range(5)  # range(0, 5)
print(test)
for _ in range(5): # просто хороший тон, когда переменная не важна
    print('Hello')
