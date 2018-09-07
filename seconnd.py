"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Первый - использовать алгоритм решето Эратосфена.
Второй - без использования "решета".
Проанализировать скорость и сложность алгоритмов.
"""
import math

# 1. Решето


def sieve_generator(num, list):
    for i in range(len(list)):
        if num % list[i] == 0:
            return 0
    return num


def simple():
    n = int(input('Введите номер простого числа:  '))
    res = [2]
    sieve = [0, 2]
    i = 2
    while len(res) < n:
        sieve.append(sieve_generator(i, res))
        i += 1
        if sieve[-1] != 0:
            res.append(sieve[-1])
    return res[-1]


# print('\n', simple())

# 2. Без решета не получилось(((

