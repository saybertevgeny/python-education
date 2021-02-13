# List comprehension

greeting = 'hello!'
letter_list = []
for letter in greeting:
    letter_list.append(letter)
print(letter_list)  # ['h', 'e', 'l', 'l', 'o', '!']

letter_list = [letter for letter in greeting]  # Тоже самое что и выше, только компактно
print(letter_list)  # ['h', 'e', 'l', 'l', 'o', '!']

number_list = [number for number in '0123456789']  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(number_list)

number_list_1 = [num for num in range(0, 9)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(number_list_1)

number_list_2 = [num ** 2 for num in range(0, 9)]
print(number_list_2)  # [0, 1, 4, 9, 16, 25, 36, 49, 64]

number_list_3 = [- ((num - 3) / 2) ** 2 for num in range(0, 9)]
print(number_list_3)  # [-2.25, -1.0, -0.25, -0.0, -0.25, -1.0, -2.25, -4.0, -6.25]

number_list = [6, 43, -2, 11, -55, -12, 3, 345]
new_list = [number for number in number_list if number > 0]
print(new_list)  # [6, 43, 11, 3, 345]

new_list_1 = ['+' if number > 0 else '_' for number in number_list]
print(new_list_1)  # ['+', '+', '_', '+', '_', '_', '+', '+']
