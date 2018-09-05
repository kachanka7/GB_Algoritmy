"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из
чисел в диапазоне от 2 до 9.
"""

num_list = []
c = 0
for i in range(2, 100):
    num_list.append(i)

for j in num_list:
    if (num_list[j - 2] % 2 == 0) or (num_list[j - 2] % 3 == 0) or (num_list[j - 2] % 5 == 0) or (
            num_list[j - 2] % 7 == 0):
        c += 1

print(c)
