'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

from collections import deque

def generate_graph(num):
    graph = {}

    for i in range(num):
        graph[i] = tuple(j for j in range(num) if j != i)

    return f'{graph}'

def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]
    deq = deque([start])
    is_visited[start] = True

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:
        curent = deq.pop()

        if curent == finish:
            break

        for i, vertex in enumerate(graph[curent]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = curent
                deq.appendleft(i)
    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'кратчайший путь {list(way)} длинною в {cost} условных единиц'

n = int(input("Количество вершин в графе: "))
s = int(input("Введите вершину начала: "))
f = int(input("Введите вершину конца: "))

g = generate_graph(n)
print(generate_graph(n))
print(bfs(g, s, f))
