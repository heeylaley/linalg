import numpy as np
import sys


def begin():
    try:
        num = int(input('Число неизвестных = '))
        return num
    except ValueError:
        print("Введите правильные данные (Нужно ввести\033[1m число\033[0;0m)")
        return begin()


n = begin()
a = np.zeros((n, n + 1))
x = np.zeros(n)


def input_num(num, matrix):
    try:
        for el in range(num):
            for elel in range(num + 1):
                a[el][elel] = float(input('a[' + str(el) + '][' + str(elel) + ']= '))
    except ValueError:
        print("Введите правильные данные (Нужно ввести\033[1m число\033[0;0m)")
        return input_num(num, matrix)


print('Введите коэффиценты, где последний коэффициент это правая часть уравнения (= ...):')
input_num(n, a)

for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Деление на ноль. Пока)))')

    for j in range(i + 1, n):
        ratio = a[j][i] / a[i][i]

        for k in range(n + 1):
            a[j][k] = a[j][k] - ratio * a[i][k]

x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    x[i] = a[i][n]

    for j in range(i + 1, n):
        x[i] = x[i] - a[i][j] * x[j]

    x[i] = x[i] / a[i][i]

print('\nРешение СЛАУ: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')
