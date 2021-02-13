nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13]]
print(nested_list)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13]]
print(len(nested_list))  # 4
print(len(nested_list[2]))  # 3
print(len(nested_list[-1]))  # 4
# Get 5
print(nested_list[1][1])  # 5
# Get 12
print(nested_list[3][2])  # 12
print(nested_list[-1][2])  # 12
print(nested_list[-1][-2])  # 12

# Print nested_list
for inner_list in nested_list:
    for number in inner_list:
        print(number)  # Просто печатаем все

[[print(number) for number in inner_list] for inner_list in nested_list]  # Тоже все печатаем только короче
