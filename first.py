"""
Проанализировать скорость и сложность одного - трёх любых алгоритмов,
разработанных в рамках домашнего задания первых трех уроков.
"""

# В качетве исследуемой фунции я решил взять новую:
# Ей будет функция вычисления факториала числа.

import timeit
import math as mh
import sys
import os
import cProfile


"""
# 1. Рекурсия
"""


def fact_rec(n):
    if n == 0:
        return int(1)
    else:
        return n * fact_rec(n - 1)


# 100 loops, best of 5: 34.4 usec per loop      - 100
# 100 loops, best of 5: 75.1 usec per loop      - 200
# 100 loops, best of 5: 675 usec per loop       - 900

# cProfile.run('fact_rec(200)')
# 201/1    0.000    0.000    0.000    0.000 first.py:21(fact_rec)


"""
# 2. Циклы-Массивы
"""


def fact_loop(n):
    factorial_arr = [i for i in range(1, n + 1)]
    f = 1
    for j in factorial_arr:
        f = f * factorial_arr[j - 1]
    return f


# 100 loops, best of 5: 29.5 usec per loop      - 100
# 100 loops, best of 5: 56 usec per loop        - 200
# 100 loops, best of 5: 668 usec per loop       - 1000

# cProfile.run('fact_loop(200)')
# 1    0.000    0.000    0.000    0.000 first.py:37(fact_loop)



"""
# 3. Массив значений факториала (словарь)
"""


def fact_dict(n):
    f_dict = {0: 1, 1: 1}

    def _fact_dict(n):
        for i in range(n):
            if n in f_dict:
                return f_dict[n]
            else:
                f_dict[n] = _fact_dict(n - 1) * n

    return _fact_dict(n)


# 100 loops, best of 5: 92.3 usec per loop      - 100
# 100 loops, best of 5: 192 usec per loop       - 200
# 100 loops, best of 5: 1.4 msec per loop       - 900

# cProfile.run('fact_dict(200)')
# 200/1    0.001    0.000    0.001    0.001 first.py:58(_fact_dict)


"""
# 4. Встроенная функция факториала библиотеки Math
"""


def fact_mh(n):
    return mh.factorial(n)

# 100 loops, best of 5: 3.5 usec per loop       - 100
# 100 loops, best of 5: 9.25 usec per loop      - 200
# 100 loops, best of 5: 216 usec per loop       - 1000

# cProfile.run('fact_mh(200)')
# 1    0.000    0.000    0.000    0.000 first.py:78(fact_mh)


"""
Данные эксперименты наглядно показывают, что вычисление одного и того же значния факториала может занимать
различные временные ресурсы у ЭВМ. Также можно отметить отличную оптимизацию стандартной библиотеки math, 
показавшей наилучший результат в скорости вычислений! 
"""