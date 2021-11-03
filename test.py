from timeit import timeit
from random import randint


def konkat(i):
    spam = ''
    for _ in range(i):
        eggs = chr(randint(0, 255))
        spam += eggs
    return spam


def list_summ(i):
    spam = []
    for _ in range(i):
        eggs = chr(randint(0, 255))
        spam.append(eggs)
    return ''.join(spam)


if __name__ == '__main__':
    print(timeit('konkat(100)',
                 setup='from __main__ import konkat',
                 number=10000))
    print(timeit('list_summ(100)',
                 setup='from __main__ import list_summ',
                 number=10000))

