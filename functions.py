#  Функции от преподователя

import sympy
from random import randint as rnd


def create_polinom(k: int, simple: bool = True) -> str:
    """Генерирует полином со случайными коэффицентами степени К
    simple = False вернет полином без сокращения нулевых коэффицентов"""
    polinom = ''
    for i in range(k, -1, -1):
        polinom += f'{rnd(0,2)}*x**{i}+'
        if i == 0:
            polinom += f'{rnd(0,100)}'
    if simple:
        return str(sympy.simplify(polinom))
    else:
        return str(polinom)


def create_pol_file(polinom: str, filename: str = 'new'):
    """Записывает полином в файл, дополнительно можно указать имя файла"""
    with open(f'Дз_4/{filename}.txt', 'w') as f:
        f.write(polinom)
