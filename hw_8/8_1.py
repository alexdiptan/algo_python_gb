# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib


def find_substr(s):
    n = len(s)
    r = set()
    for i in range(n):
        if i == 0:
            n = len(s) - 1
        else:
            n = len(s)
        for j in range(n, i, -1):
            print(s[i:j])
            r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    return r


if __name__ == '__main__':
    start_string = 'santa'
    print(f"Количество подстрок в строке '{start_string}' = {len(find_substr(start_string))}")

"""
output:
sant
san
sa
s
anta
ant
an
a
nta
nt
n
ta
t
a
Количество подстрок в строке 'santa' = 13

Process finished with exit code 0

"""
