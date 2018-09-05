"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
позицию в массиве.
"""

import random
rand_list = []
for i in range(20):
    rand_list.append(random.randint(-99, 99))
print('\n', rand_list)
print('\nМинимальный элемент: ', min(rand_list), "Его позиция:  ", rand_list.index(min(rand_list)))