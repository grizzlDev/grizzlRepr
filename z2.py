my_list = [9, 2, 1, 6, 7, 5, 4, 8]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Результат {new_list}')