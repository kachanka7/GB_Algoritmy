"""
Во втором массиве сохранить индексы четных элементов первого массива. Например, если
дан массив со значениями 8, 3, 15, 6, 4, 2, то второй массив надо заполнить значениями 1, 4,
5, 6 (или 0, 3, 4, 5 – если индексация начинается с нуля), так как именно в этих позициях
первого массива стоят четные числа.
"""

list_1 = [1, 2, 3, 4, 6, 6, 8, 10, 11, 13, 22]
list_chet = []
for i in range(len(list_1)):
    if (int(list_1[i]) % 2 == 0):
        list_chet.append(i)
print(list_chet)
