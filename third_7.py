"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найти в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
"""
import random

m = int(input('\nВведите размерность массива м:  '))

arr = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив:\n{arr}')

# без сортировки пробовал, однако попытки успехом не увенчалось( требудется больше времмени на решение)

arr.sort()
print(f'Сортированный список: \n{arr}')
print(f'Медиана списка = {arr[m]}')