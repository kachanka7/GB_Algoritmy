"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
В конце следует вывести полученную матрицу.
"""


# Возникли проблемы с подключением данной билиотеки. Хотя была установлена через pip
# import numpy as np


# Функция вычисления суммы элементов одномерного массива
def summa(list):
    summ = 0
    for i in range(len(list)):
        summ += int(list[i])
    return summ


column = 5
line = 5

arr = []
q = 1
for i in range(line):
    arr.append([])
    for j in range(column - 1):
        arr[i].append(int(input("\nВведите элемент массива[{}][{}]: ".format(i, j))))
        if j == 3:
            arr[i].append(summa(arr[i]))

print('\n\n')

for i in range(5):
    print(arr[i])
