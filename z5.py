result = 0
while True:
    line = input("Введите числа, для выхода нажмите 'а' англ: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == 'a':
                print(f"Сумма {result}.")
                exit(0)
            else:
                print(f"Сумма {result}. Ошибка")
                exit(1)
print(result)
exit()
