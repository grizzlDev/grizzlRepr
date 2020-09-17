from functools import reduce


def my_func(el_p, el):
    return el_p * el


print(f'Список значений {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Перемножения всех элементов {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')
