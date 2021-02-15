print(1, end=' ')
print(2, end='')  # 12
print("#####")


def func(a, b=2, c=3):
    print(a, b, c)


func(1, 2, 3)  # 1 2 3
func(1, c=20)  # 1 2 20
c = 100


def func1(*params):
    global c
    c = 0
    print(params)
    print(type(params))  # <class 'tuple'>


func1(1, 2, 3, 4, 5, 6, 7)  # (1, 2, 3, 4, 5, 6, 7)
print(c)


def func2(**params):
    '''
    help on function
    for example in python console:
    :param params:
    :return: NONE
    '''
    print(params)
    print(type(params))  # <class 'dict'>


func2(Mike=1, John=2)  # {'Mike': 1, 'John': 2}
# func2(1,2,3) # ошибка
help(func2)  # func2(**params)


# help on function
# for example in python console:
#:param params:
#:return:


# Lambda function
def multiple_x2(x):
    return x + x


number_list = [1, 2, 3, 4, 5]

result = map(multiple_x2, number_list)
print(result)  # <map object at 0x0000028AF9D98FA0>
for item in result: print(item)  # 2 4 6 .. 10
print(list(map(multiple_x2, number_list)))  # [2, 4, 6, 8, 10]


def is_a_in_string(str):
    if 'a' in str:
        print("String has 'a'")
        return True
    else:
        print("String has not 'a'")
        return False


str_list = ['hi', 'was', 'name', 'he']
print(list(map(is_a_in_string,
               str_list)))  # String has not 'a' .... String has not 'a'  и вывод самой функции [False, True, True, False]


def is_number_odd(number):
    return number % 2 == 1


number_list = list(range(10))
print(list(filter(is_number_odd, number_list)))  # [1, 3, 5, 7, 9]


def cube(number): return number ** 3  # корректно но не надо


print(list(map(cube, number_list)))  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

print(list(map(lambda number: number ** 3, number_list)))  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

print(list(filter(lambda number: number % 2 == 0, number_list)))  # [0, 2, 4, 6, 8]
