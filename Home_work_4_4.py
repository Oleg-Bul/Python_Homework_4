# 4'. Задана натуральная степень k. Сформировать случайным образом
#  список коэффициентов (значения от 0 до 100)
#  многочлена и записать в файл многочлен степени k.(записать в строку)
# Пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5


import random

k = int(input(' Введите степень "k": '))

MnogoChlenList = []
for i in range(1, k, 1):
    randCoeff = random.randint(0, 100)
    MnogoChlenList.insert(0, (i+1))
    MnogoChlenList.insert(0, '*x**')
    MnogoChlenList.insert(0, randCoeff)
    MnogoChlenList.insert(0, ' + ')
MnogoChlenList.remove(' + ')
MnogoChlenList.append(' + ')
MnogoChlenList.append(str(randCoeff)+'x')
MnogoChlenList.append(' + ')
MnogoChlenList.append(random.randint(0, 100))

# print(MnogoChlenList)
MnogoChlen = ("".join(map(str, MnogoChlenList)))
print(MnogoChlen)

# Очень не оптимально, но работает)
