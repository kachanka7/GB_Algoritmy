"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

rand_list = []
for i in range(int(input("\nВведите число элементо в массива:   "))):
    rand_list.append(random.randint(0, 99))

print('\n', rand_list)
mx = max(rand_list)
mn = min(rand_list)
mn_ind = rand_list.index(mn)
mx_ind = rand_list.index(mx)
print("\nmin = {}({}), max = {}({})".format(mn, mn_ind, mx, mx_ind))
sum = 0
if mn_ind > mx_ind:
    a = mx_ind
    b = mn_ind
else:
    a = mn_ind
    b = mx_ind

for j in range(len(rand_list)):
    if (j > a) and (j < b):
        sum += rand_list[j]
    else:
        continue

print('\n Результат суммы: ', sum)
