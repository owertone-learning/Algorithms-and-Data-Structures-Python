'''
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
'''

two, three, four, five, six, seven, eight, nine = (0,) * 8
two_list, three_list, four_list, five_list, six_list, seven_list, eight_list, nine_list = ([] for i in range(8))

for i in range(2, 100):
    if i % 2 == 0:
        two += 1
        two_list.append(i)
    if i % 3 == 0:
        three += 1
        three_list.append(i)
    if i % 4 == 0:
        four += 1
        four_list.append(i)
    if i % 5 == 0:
        five += 1
        five_list.append(i)
    if i % 6 == 0:
        six += 1
        six_list.append(i)
    if i % 7 == 0:
        seven += 1
        seven_list.append(i)
    if i % 8 == 0:
        eight += 1
        eight_list.append(i)
    if i % 9 == 0:
        nine += 1
        nine_list.append(i)

print(f'{two} чисел кратны 2, это числа {two_list}\n{three} чисел кратны 3, это числа {three_list}\n'
      f'{four} чисел кратны 4, это числа {four_list}\n{five} чисел кратны 5, это числа {five_list}\n'
      f'{six} чисел кратны 6, это числа {six_list}\n{seven} чисел кратны 7, это числа {seven_list}\n'
      f'{eight} чисел кратны 8, это числа {eight_list}\n{nine} чисел кратны 9, это числа {nine_list}\n')
