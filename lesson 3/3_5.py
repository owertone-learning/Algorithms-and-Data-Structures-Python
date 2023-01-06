'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
'''

import random

lst = [random.randint(-20, 20) for _ in range(30)]
print(lst)
max_number = -float('inf')
max_index = 0
for i, item in enumerate(lst):
    if item < 0:
        if item > max_number:
            max_number = item
            max_index = i
print(max_number, max_index)
