'''
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
первых трех уроков. Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
'''

'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
'''
import cProfile
import timeit

def count_for(max_number):
    two, three, four, five, six, seven, eight, nine = (0,) * 8
    for i in range(2, max_number + 1):
        if i % 2 == 0:
            two += 1
        if i % 3 == 0:
            three += 1
        if i % 4 == 0:
            four += 1
        if i % 5 == 0:
            five += 1
        if i % 6 == 0:
            six += 1
        if i % 7 == 0:
            seven += 1
        if i % 8 == 0:
            eight += 1
        if i % 9 == 0:
            nine += 1
    return two, three, four, five, six, seven, eight, nine

# 1000 loops, best of 5: 29.9 usec per loop //  max_number 99
# 1000 loops, best of 5: 307 usec per loop  //  max_number 999
# 1000 loops, best of 5: 23 msec per loop   //  max_number 99999
# 1000 loops, best of 5: 232 msec per loop  //  max_number 999999

cProfile.run('count_for(99)')

# 1    0.000    0.000    0.000    0.000 task4_1.py:17(count_for) //  max_number 99
# 1    0.000    0.000    0.000    0.000 task4_1.py:17(count_for) //  max_number 999
# 1    0.046    0.046    0.046    0.046 task4_1.py:17(count_for) //  max_number 99999
# 1    0.337    0.337    0.337    0.337 task4_1.py:17(count_for) //  max_number 999999
# 1   32.063   32.063   32.063   32.063 task4_1.py:17(count_for) //  max_number 99999999

def count_while(max_number):
    two, three, four, five, six, seven, eight, nine = (0,) * 8
    i = 2
    while i < max_number + 1:
        if i % 2 == 0:
            two += 1
        if i % 3 == 0:
            three += 1
        if i % 4 == 0:
            four += 1
        if i % 5 == 0:
            five += 1
        if i % 6 == 0:
            six += 1
        if i % 7 == 0:
            seven += 1
        if i % 8 == 0:
            eight += 1
        if i % 9 == 0:
            nine += 1
        i += 1
    return two, three, four, five, six, seven, eight, nine

# 1000 loops, best of 5: 29.9 usec per loop //  max_number 99
# 1000 loops, best of 5: 314 usec per loop  //  max_number 999
# 1000 loops, best of 5: 27.1 msec per loop //  max_number 99999
# 1000 loops, best of 5: 263 msec per loop  //  max_number 999999

cProfile.run('count_while(99)')

# 1    0.000    0.000    0.000    0.000 task4_1.py:51(count_while) //  max_number 99
# 1    0.001    0.001    0.001    0.001 task4_1.py:51(count_while) //  max_number 999
# 1    0.040    0.040    0.040    0.040 task4_1.py:51(count_while) //  max_number 99999
# 1    0.384    0.384    0.384    0.384 task4_1.py:51(count_while) //  max_number 999999
# 1   35.997   35.997   35.997   35.997 task4_1.py:51(count_while) //  max_number 99999999

def count_for_dict(max_number):
    min_num = 2
    max_num = 9
    data_num = dict()
    for item in range(min_num, max_num + 1):
        data_num[item] = max_number // item
    return data_num

# 1000 loops, best of 5: 705 nsec per loop //  max_number 99
# 1000 loops, best of 5: 707 nsec per loop  //  max_number 999
# 1000 loops, best of 5: 734 nsec per loop   //  max_number 99999
# 1000 loops, best of 5: 749 nsec per loop  //  max_number 999999

cProfile.run('count_for_dict(99)')

# 1    0.000    0.000    0.000    0.000 task4_1.py:87(count_for_dict) //  max_number 99
# 1    0.000    0.000    0.000    0.000 task4_1.py:87(count_for_dict) //  max_number 999
# 1    0.000    0.000    0.000    0.000 task4_1.py:87(count_for_dict) //  max_number 99999
# 1    0.000    0.000    0.000    0.000 task4_1.py:87(count_for_dict) //  max_number 999999
# 1    0.000    0.000    0.000    0.000 task4_1.py:87(count_for_dict) //  max_number 99999999


'''
Функции count_for() и count_while(), по сути выполняя перебор, на при небольших вычислениях работают примерно
одинаково. С возрастанием сложности count_for() начинает работать чуть быстрее. Зависимость времени от сложности
похожа на линейную, но, мне кажется, что с ростом сложности линейная зависимость станет экспоненциальной.
Функция count_for_dict() реализованная с помощью словаря практически не чувствует нарастания сложности - даже при 
росте сложности на несколько порядков время работы функции заметно не отличается. Великолепный результат.

Вывод - функция count_for_dict() работает отлично с большим отрывом от двух других.
'''