# 3'. Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной
#  последовательности.

List1 = input('Введите спискок: ').split()
List1 = [i for i in List1]
print('Ваш список :', List1)


def remove_repeat(nums: list) -> list:
    """Удаляет одинаковые элементы в списке"""
    temp = []
    for x in nums:
        if x not in temp:
            temp.append(x)
    nums = temp
    return nums


print('Список без дубликатов: ', remove_repeat(List1))
