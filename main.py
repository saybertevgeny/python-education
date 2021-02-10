# Dictionaries можно получить по ключу

car_prices = {"Opel": 5000, "Toyota": 7000, "BMW": 10000}
print(car_prices)  # {'Opel': 5000, 'Toyota': 7000, 'BMW': 10000}
print(car_prices["Toyota"])  # 7000
car_prices['Mazda'] = 4000
print(car_prices)  # {'Opel': 5000, 'Toyota': 7000, 'BMW': 10000, 'Mazda': 4000}
car_prices['Opel'] = 2000
print(car_prices)  # {'Opel': 2000, 'Toyota': 7000, 'BMW': 10000, 'Mazda': 4000}

del car_prices['Toyota']
print(car_prices)  # {'Opel': 2000, 'BMW': 10000, 'Mazda': 4000}
# del car_prices
# print(car_prices)  #Ошибка car_prices уже удалили
car_prices.clear()
print(car_prices)  # {} удалили все элементы

person = {
    'first name': "Jack",
    "last name": "Brown",
    'age': 23,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {
        'son': 'Mickle',
        'daugter': 'Pamela'
    }
}
print(person['age'])  # 23
print(person['hobbies'])  # ['football', 'singing', 'photo']
hobbies = person['hobbies']
print(hobbies[2])  # photo
print(person['hobbies'][2])  # photo
print(person['children']['son'])  # Mickle
print(person.keys())  # dict_keys(['first name', 'last name', 'age', 'hobbies', 'children'])
print(person.values())  # dict_values(['Jack', 'Brown', 23, ['football', 'singing', 'photo'], {'son': 'Mickle', 'daugter': 'Pamela'}])
print(person.items())  # dict_items([('first name', 'Jack'), ('last name', 'Brown'), ('age', 23), ('hobbies', ['football', 'singing', 'photo']), ('children', {'son': 'Mickle', 'daugter': 'Pamela'})]) вот это называется Tuples
