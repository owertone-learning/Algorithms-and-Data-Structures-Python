'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
'''

from collections import deque
from collections import namedtuple

Company = namedtuple('Company', 'name profit1 profit2 profit3 profit4 total_profit')
company_number = int(input('Введите число компаний: '))

companies = []
total_income = 0
profit_company = deque()
none_profit_company = deque()

for i in range(company_number):
    name = input(f'Введите название {i + 1} компании: ')
    profit1 = float(input(f'Прибыль компании {i + 1} в первом квартале: '))
    profit2 = float(input(f'Прибыль компании {i + 1} во втором квартале: '))
    profit3 = float(input(f'Прибыль компании {i + 1} в третьем квартале: '))
    profit4 = float(input(f'Прибыль компании {i + 1} в четвертом квартале: '))
    total_profit = profit1 + profit2 + profit3 + profit4
    total_income += total_profit
    companies.append(Company(name, profit1, profit2, profit3, profit4, total_profit))

average_income = total_income / company_number

print('-' * 50)
print(f'Cредняя прибыль по всем компаниям: {average_income}')
print('-' * 50)

for company in companies:
    if company.total_profit > average_income:
        profit_company.append(company.name)
    else:
        none_profit_company.append(company.name)

print(f'Компании, чья прибыль выше среднего: {", ".join(str(element) for element in profit_company)}')
print(f'Компании, чья прибыль ниже среднего: {", ".join(str(element) for element in none_profit_company)}')
