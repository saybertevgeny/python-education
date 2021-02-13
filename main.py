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
    :return:
    '''
    print(params)
    print(type(params))  # <class 'dict'>


func2(Mike=1, John=2)  # {'Mike': 1, 'John': 2}
# func2(1,2,3) # ошибка
help(func2) #func2(**params)
            #help on function
            #for example in python console:
            #:param params:
            #:return:
