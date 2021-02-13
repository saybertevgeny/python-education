x = 1

while x > 1:
    print(x)  # Не запуститься
else:
    print("x now is less or equal than 10")

for x in range(10):
    print(str(x) + " x is less than 10")  # 0 x is less than 10...
else:
    x += 1
    print(str(x) + " x not is less than 10")  # 10 x not is less than 10

# break, continue, pass
my_list = [1, 2, 3]
for item in my_list:
    pass  # просто ничего не делает, просто заполнить пустоты, если его убрать то будет ошибка

print('Another code')
