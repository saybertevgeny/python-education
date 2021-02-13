# Set comprehension
number_list = [6, 43, 0, -2, 11, -55, -12, 3, 345]
number_set = {number ** 2 for number in number_list}
print(number_set)  # {0, 121, 36, 4, 9, 144, 3025, 119025, 1849}

number_set = {number ** 2 for number in range(10)}
print(number_set)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

letter_set = {letter.upper() for letter in 'hello'}
print(letter_set)  # {'L', 'H', 'E', 'O'}
