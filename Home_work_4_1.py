# 1'. Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  


import math
d = str(input('Введите точночть "d": '))
count = len(str(d)) - 2
print('Число пи с точность ', count, 'знаков после запятой = ', round(math.pi, count))
