'''
4. Определить, какое число в массиве встречается чаще всего.
'''

import random

lst = [random.randint(0, 10) for _ in range(30)]
print(lst)
list_set = set(lst)
most_common = None
num_most_common = 0
for item in list_set:
    qty = lst.count(item)
    if qty > num_most_common:
        num_most_common = qty
        most_common = item
print(f'Число {most_common} встречается чаще всего раз - {num_most_common}')
