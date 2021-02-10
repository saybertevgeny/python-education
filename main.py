number_list = [32, 21, 48, 34.56]
print(number_list)  # [32, 21, 48, 34.56]
some_list = [12, 35.334, "Hello"]
print(some_list)  # [12, 35.334, 'Hello']
print(len(some_list))  # 3
print(some_list[1])  # 35.334
another_list = some_list[:2]
some_list[2] = "hi"
print(some_list)  # [12, 35.334, 'hi']
some_list[1] = 44
print(another_list)  # [12, 35.334]

# Adding and removing Items
new_list = some_list + another_list
print(new_list)  # [12, 44, 'hi', 12, 35.334]
# new_list[5] = 'new item' # ошибка присовоению индексу за переделами листа
new_list.append("new item")  # тут все корректно
print(new_list)  # [12, 44, 'hi', 12, 35.334, 'new item']
new_list.insert(0, "start")
print(new_list)  # ['start', 12, 44, 'hi', 12, 35.334, 'new item']

print(new_list.pop())  # new item
print(new_list)  # ['start', 12, 44, 'hi', 12, 35.334] т.у. pop удалил из списка
new_list.pop(2)
print(new_list)  # ['start', 12, 'hi', 12, 35.334]

deleted_item = new_list.remove(12)  # удаляет по значению первое
print(new_list)  # ['start', 'hi', 12, 35.334]
print(deleted_item)  # None - пустота

number_list = [45, 12, 3, -455, 22]
letter_list = ['s', 'w', 't', 'a']
print(number_list)  # [45, 12, 3, -455, 22]
print(letter_list)  # [45, 12, 3, -455, 22]
new_list = letter_list
x = number_list.sort()
y = letter_list.sort()
print(number_list)  # [-455, 3, 12, 22, 45]
print(letter_list)  # ['a', 's', 't', 'w']
print(x)  # None
print(y)  # None
print(new_list)  # ['a', 's', 't', 'w'] т.е. по ссылке

number_list.reverse()
letter_list.reverse()
print(number_list)  # [45, 22, 12, 3, -455]
print(letter_list)  # ['w', 't', 's', 'a']

number_list.append(letter_list)
print(number_list)  # [45, 22, 12, 3, -455, ['w', 't', 's', 'a']]
