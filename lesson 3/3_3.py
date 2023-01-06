'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random

list_1 = [random.randint(0, 20) for _ in range(20)]
max_number = list_1[0]
min_number = list_1[0]
max_index, min_index = 0, 0
print(list_1)
for i, item in enumerate(list_1):
    if item > max_number:
        max_number = item
        max_index = i
    if item < min_number:
        min_number = item
        min_index = i
list_2 = list_1.copy()
list_2[min_index] = max_number
list_2[max_index] = min_number
print(list_2)
