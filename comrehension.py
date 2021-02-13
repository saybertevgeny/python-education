number_dict = {'first': 1, 'second': 2, 'third': 3}
new_dict = {key: value ** 3 for key, value in number_dict.items()}
print(new_dict)  # {'first': 1, 'second': 8, 'third': 27}

number_list = [6, 43, -2, 11, -55, 0, -12, 3, 345]
number_dict = {number: number ** 2 for number in number_list}
print(number_dict)  # {6: 36, 43: 1849, -2: 4, 11: 121, -55: 3025, 0: 0, -12: 144, 3: 9, 345: 119025}

number_dict = {number: 'positive' if number > 0 else 'negative' if number < 0 else 'zero' for number in number_list}
print(number_dict)  # {6: 'positive', 43: 'positive', -2: 'negative', 11: 'positive', -55: 'negative', 0: 'zero', -12: 'negative', 3: 'positive', 345: 'positive'}
