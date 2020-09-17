my_list = [0, 2, 1, 3, 1, 2, 5, 4, 6, 5, 4, 3]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)