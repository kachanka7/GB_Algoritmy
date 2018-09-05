"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

a = int(input("\nВведите число элементов массива:  "))

rnd_lst = []
for i in range(int(a)): rnd_lst.append(random.randint(0, 10))
print(rnd_lst)
num = rnd_lst[0]
mx_freq = 1

for i in range(a - 1):
    freq = 1
    for j in range(i + 1, a):
        if rnd_lst[i] == rnd_lst[j]:
            freq += 1
    if freq > mx_freq:
        mx_freq = freq
        num = rnd_lst[i]

print('Число {} встречается чаще остальных'.format(num))