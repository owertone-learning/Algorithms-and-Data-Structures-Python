'''
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
'''
number = int(input('Введите натуральное число: '))
numbers = ''
while number > 0:
    numbers += str(number % 10)
    number //= 10
print(f'Обратное по порядку: {int(numbers)}')
