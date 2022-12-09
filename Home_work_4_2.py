# 2'. Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

x = int(input('Введите число: '))


def PrimeFactors(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


def RemoveRepeat(nums: list) -> list:
    """Удаляет одинаковые элементы в списке"""
    temp = []
    for x in nums:
        if x not in temp:
            temp.append(x)
    nums = temp
    return nums


print(RemoveRepeat(PrimeFactors(x)))


# #Решение от преподователя
# def dividers(a: int, uniq: bool = False) -> list[int]:
#     """"Возвращает список простых делителей числа.
#     uniq = True вернет список уникальных делителей"""
#     i = 2
#     dividers = []
#     while a != 1:
#         while a % i == 0:
#             dividers.append(i)
#             a //= i
#         i += 1
#     if uniq:
#         return list(set(dividers))
#     else:
#         return dividers


# a = 81
# print(f'Список натуральных делителей числа {a}:{dividers(a)}')
# print(f'Список уникальных делителей числа {a}:{dividers(a, True)}')