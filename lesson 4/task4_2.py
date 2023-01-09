'''
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
'''
import math
from math import sqrt
import cProfile

# нахождение i-го по счёту простого числа с помощью алгоритма «Решето Эратосфена»
def sieve_erato(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result


# cProfile.run('sieve_erato (100000)')
#print(sieve_erato(40))
# 1    0.000    0.000    0.000    0.000 task4_2.py:15(sieve_erato) //  n = 10
# 1    0.000    0.000    0.000    0.000 task4_2.py:15(sieve_erato) //  n = 100
# 1    0.000    0.000    0.000    0.000 task4_2.py:15(sieve_erato) //  n = 1000
# 1    0.002    0.002    0.002    0.002 task4_2.py:15(sieve_erato) /  n = 10000
# 1    0.025    0.025    0.030    0.030 task4_2.py:15(sieve_erato // n = 100000

# python -m timeit -n 1000 -s "import task4_2" "task4_2.sieve_erato(10)"
# 1000 loops, best of 5: 2.8 usec per loop
# python -m timeit -n 1000 -s "import task4_2" "task4_2.sieve_erato(1000)"
# 1000 loops, best of 5: 171 usec per loop
# python -m timeit -n 1000 -s "import task4_2" "task4_2.sieve_erato(100000)"
# 1000 loops, best of 5: 18.8 msec per loop

# нахождение i-го по счёту простого числа без использования «Решета Эратосфена»
def sieve_none_erato(n):
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst


#cProfile.run('sieve_none_erato (100000)')
#print(sieve_none_erato(10))

# 1    0.000    0.000    0.000    0.000 task4_2.py:43(sieve_none_erato) //  n = 10
# 1    0.000    0.000    0.000    0.000 task4_2.py:43(sieve_none_erato) //  n = 100
# 1    0.000    0.000    0.000    0.000 task4_2.py:45(sieve_none_erato) //  n = 1000
# 1    0.007    0.007    0.007    0.007 task4_2.py:45(sieve_none_erato) //  n = 10000
# 1    0.064    0.064    0.065    0.065 task4_2.py:45(sieve_none_erato) //  n = 100000

# python -m timeit -n 1000 -s "import task4_2" "task4_2.sieve_none_erato(10)"
# 1000 loops, best of 5: 1 usec per loop
# python -m timeit -n 1000 -s "import task4_2" "task4_2.sieve_none_erato(1000)"
# 1000 loops, best of 5: 195 usec per loop
# python -m timeit -n 1000 -s "import task4_2" "task4_2.sieve_none_erato(100000)"
# 1000 loops, best of 5: 53.2 msec per loop


'''
ВЫВОД
оба алгоритма отрабатывают примерно за одинаковое время, но с решетом чуть быстрее
'''
