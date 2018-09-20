"""
1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Вывести на экран исходный и отсортированный массивы.
"""

import random

arr = [random.randint(-100, 100) for _ in range(13)]
print(f'Исходный массив:   \n{arr}')

count = 1

while count < len(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    count += 1
arr.reverse()
print(f'Массив, отсортированный методома пузырька: \n{arr}')
