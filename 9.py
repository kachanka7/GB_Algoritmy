"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

col = 7
ln = 3
a = []
for i in range(ln):
    b = []
    for j in range(col):
        b.append(int(random.randint(0, 99)))
    a.append(b)

print("\n")
for i in range(ln):
    print(a[i])

mx = -1
for j in range(col):
    mn = 100
    for i in range(ln):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print("максимальный элемент среди минимальных элементов столбцов матрицы:   ", mx)
