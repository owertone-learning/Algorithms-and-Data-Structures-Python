'''
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

number = int(input('Введите натуральное число: '))
numbers = number  # сохраняем число для вывода на печать в конце выполнения программы
even_list = ''
odd_list = ''
even = 0
odd = 0
while number > 0:
    num = number % 10
    if num % 2 == 0:
        even += 1
        even_list += str(num)
    else:
        odd += 1
        odd_list += str(num)
    number //= 10

print(f'Количество нечетных цифр в числе {numbers}: {odd}, это цифры {",".join(map(str, str(odd_list)))}.\n'
      f'Количество четных цифр в числе {numbers}: {even}, это цифры {",".join(map(str, str(even_list)))}')
