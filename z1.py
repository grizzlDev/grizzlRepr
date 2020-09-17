from sys import argv

time, sta, bonus = argv
try:
    time = int(time)
    sta = int(sta)
    bonus = int(bonus)
    result = time * sta + bonus
    print(f'заработная плата состовляет:  {result}')
except ValueError:
    print('Не верно')