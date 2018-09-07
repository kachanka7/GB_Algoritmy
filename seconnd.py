"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Первый - использовать алгоритм решето Эратосфена.
Второй - без использования "решета".
Проанализировать скорость и сложность алгоритмов.
"""
import math
import cProfile


# 1. Решето


def sieve_generator(num, list):
    for i in range(len(list)):
        if num % list[i] == 0:
            return 0
    return num


def simple(n):
    # n = int(input('Введите номер простого числа:  '))
    res = [2]
    sieve = [0, 2]
    i = 2
    while len(res) < n:
        sieve.append(sieve_generator(i, res))
        i += 1
        if sieve[-1] != 0:
            res.append(sieve[-1])
    return res[-1]


# cProfile.run('simple(500)')
# 3570    0.020    0.000    0.021    0.000 seconnd.py:14(sieve_generator)
# 7141    0.001    0.000    0.001    0.000 {built-in method builtins.len}
# 4069    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# 2. Без решета не получилось(((
