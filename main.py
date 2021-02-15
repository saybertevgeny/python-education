pi = 'outer pi variable'


def print_pi():
    pi = 'inner pi variable'
    print(pi)


print_pi()  # inner pi variable
print(pi)  # outer pi variable

pi_1 = 'outer pi variable'


def print_pi_1():
    print(pi_1)


print_pi_1()  # outer pi variable
print(pi_1)  # outer pi variable

pi_2 = "global pi variable"


def outer():
    pi_2 = "outer pi variable1"
    print(pi_2)  # outer pi variable1

    def inner():
        nonlocal pi_2
        print(pi_2)  # outer pi variable1

    inner()


outer()
print(pi_2)  # global pi variable

pi_3 = "global pi variable"


def outer():
    pi_3 = "outer pi variable3"
    print(pi_3)  # outer pi variable3

    def inner():
        global pi_3
        print(pi_3)  # global pi variable

    inner()


outer()
print(pi_3)  # global pi variable

from math import pi as pi


def outer_1():
    def inner():
        print(pi)  # 3.141592653589793

    inner()


outer_1()
