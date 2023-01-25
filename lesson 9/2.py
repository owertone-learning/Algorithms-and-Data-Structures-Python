'''
2. Закодируйте любую строку по алгоритму Хаффмана.
'''

s = input('Введите строку: ')


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


def huffman(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman(l, True, binString + '0'))
    d.update(huffman(r, False, binString + '1'))
    return d


freq = {}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman(nodes[0][0])


def code_of_string():
    code = ''
    for char in s:
        code += str(huffmanCode[char]) + ' '
    return code


print(f'Строка {s} в закодированном по алгоритму Хаффмана виде: {code_of_string()}')
