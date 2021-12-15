from collections import Counter


def find_char_frequency(text):
    result = dict()
    with open(text, 'r') as f:
        for line in f.readlines():
            line = line.lower()
            for i in line:
                if i.isalpha():
                    if i in result:
                        result[i] += 1
                    else:
                        result.update({i: 1})
    print(Counter(result))
    return result


# класс узла
class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None


# дерево Хаффмана
class HuffmanTree(object):
    def __init__(self, char_weights):
        self.Leaf = [Node(k, v) for k, v in char_weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node:node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    def hu_generate(self, node, length):
        if not node:
            return
        elif node.name:
            print(f'Для буквы {node.name} код Хаффмана: ', end='')
            for i in range(length):
                print(self.Buffer[i], end='')
            print('\n')
            return
        self.Buffer[length] = 0
        self.hu_generate(node.lchild, length + 1)
        self.Buffer[length] = 1
        self.hu_generate(node.rchild, length + 1)

    def get_code(self):
        self.hu_generate(self.root, 0)


if __name__ == '__main__':
    txt = r'1.txt'
    res = find_char_frequency(txt)
    tree = HuffmanTree(res)
    tree.get_code()

"""
Код взял в интернете, и немного доработал. Добавил Counter, чтобы посчитать кол-во вхождений букв. 
output:
Counter({'e': 70, 'l': 60, 'i': 54, 'n': 42, 's': 39, 'h': 37, 't': 30, 'o': 30, 'a': 27, 'g': 24, 'j': 18, 'r': 15, 'b': 12, 'w': 12, 'y': 10, 'f': 6, 'u': 6, 'd': 6, 'p': 6, 'c': 3, 'm': 3})
Для буквы d кодировка Хаффмана: 000000

Для буквы u кодировка Хаффмана: 000001

Для буквы m кодировка Хаффмана: 0000100

Для буквы c кодировка Хаффмана: 0000101

Для буквы p кодировка Хаффмана: 000011

Для буквы g кодировка Хаффмана: 0001

Для буквы i кодировка Хаффмана: 001

Для буквы a кодировка Хаффмана: 0100

Для буквы o кодировка Хаффмана: 0101

Для буквы l кодировка Хаффмана: 011

Для буквы t кодировка Хаффмана: 1000

Для буквы r кодировка Хаффмана: 10010

Для буквы f кодировка Хаффмана: 100110

Для буквы y кодировка Хаффмана: 100111

Для буквы e кодировка Хаффмана: 101

Для буквы h кодировка Хаффмана: 1100

Для буквы s кодировка Хаффмана: 1101

Для буквы j кодировка Хаффмана: 11100

Для буквы w кодировка Хаффмана: 111010

Для буквы b кодировка Хаффмана: 111011

Для буквы n кодировка Хаффмана: 1111

"""