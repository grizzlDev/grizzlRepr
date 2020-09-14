def my_func (x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "0 быть не может"
    except ValueError:
        return "Введите только число"
print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))