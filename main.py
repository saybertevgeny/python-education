# В множестве не может быть двух одинкавых объектов
rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}
print(rainbow_colors)  # {'indigo', 'green', 'yellow', 'red', 'violet', 'blue', 'orange'}
print(type(rainbow_colors))  # <class 'set'>
empty_set = {}
print(empty_set)  # {}
print(type(empty_set))  # <class 'dict'> !не множетсво!

empty_set = set()
print(empty_set)  # set()
print(type(empty_set))  # <class 'set'>

number_list = [1, 43, 56]
test_tuple = ('sdsa', 'asda')
set_from_list = set(number_list)
set_from_tuple = set(test_tuple)
print(set_from_list)  # {56, 1, 43} - распакованные
print(set_from_tuple)  # {'asda', 'sdsa'} - распакаванные

set_from_list.add(777)
set_from_tuple.add("hello")
print(set_from_list)  # {56, 1, 43, 777}
print(set_from_tuple)  # {'hello', 'asda', 'sdsa'}

set_from_list.add(777)
print(set_from_list)  # {56, 1, 43, 777}

x = set_from_list.pop()
print(set_from_list)  # {1, 43, 777}
print(x)  # 56

y = set_from_list.remove(777)
print(set_from_list)
print(y)  # None

set_from_list.discard(43)
print(set_from_list)  # {1}
# set_from_tuple.remove(3) # Ошибка
set_from_list.discard(3)  # Ошибки нет

set_from_list.clear()
print(set_from_list, type(set_from_list))  # set() <class 'set'>
