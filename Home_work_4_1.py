# 1'. Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415


import math
d = str(input('Введите точночть "d": '))
count = len(str(d)) - 2
print('Точность ', count, 'знаков после запятой = ', round(math.pi, count))


# Решение от преподователя

# from math import pi


# def format_by_mask(num: float, accuracy: float) -> float:
#     """"форматирует число по заданной маске"""
#     accuracy = str(accuracy)
#     accuracy = len(accuracy[accuracy.find('.')+1::])
#     return float(f'{pi:0.{accuracy}f}')    # f'a:0.3f'


# d = input('Введите точность в формате "0.001": ')
# print(format_by_mask(pi, d))
