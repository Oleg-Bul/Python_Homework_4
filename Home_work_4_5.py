# 5'. Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
import sympy

with open('file1.txt', 'r') as f:
    a = f.read()
with open('file2.txt', 'r') as f:
    b = f.read()
print('(', a, ')', ' + ', '(', b, ')')

ans = sympy.sympify(a+b)
with open('file3.txt', 'a') as f:
    f.write(str(ans))
f.close
