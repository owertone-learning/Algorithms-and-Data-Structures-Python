'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''

numbers = int(input('Введите количество друзей: '))
graph = []
for i in range(numbers):
    row = [1] * numbers
    for j in range(numbers):
        if i >= j:
            row[j] = 0
    graph.append(row)

print(*graph, sep='\n')

hand = 0 #начальное количество рукопожатий равно нулю

for item in graph:
    hand += sum(item)

print(f'Количество рукопожатий {hand}')
print(f'Проверка с помощью формулы: {int(numbers*(numbers-1)/2)}')