"""
В массиве случайных целых чисел поменять местами минимальный и максимальный
элементы.
"""
import random

random_list = []
for i in range(int(input("Введите число случайных элементов массива:   "))):
    random_list.append(random.randint(0, 99))

print(random_list)
mx = max(random_list)
mn = min(random_list)
mn_ind = random_list.index(mn)
mx_ind = random_list.index(mx)

random_list.remove(mx)
random_list.insert(mn_ind, mx)
random_list.remove(mn)
random_list.insert(mx_ind, mn)

print(random_list)