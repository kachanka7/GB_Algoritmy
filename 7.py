"""
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
как равны между собой (оба являться минимальными), так и различаться.
"""
import random

rand_list1 = []
rand_list2 = []
for i in range(int(input("\nВведите число элементо в массива:   "))):
    rand_list1.append(random.randint(0, 99))
    rand_list2.append(rand_list1[i])

print("\nМассив:  ", rand_list1)
mn1 = min(rand_list1)
rand_list2.remove(mn1)
mn2 = min(rand_list2)

print("Минималные числа:  {} и {} ".format(mn1, mn2))
