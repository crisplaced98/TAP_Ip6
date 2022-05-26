from Animal import Animal
from Gato import Gato
from LoroMutante import LoroMutante

import collections
class Test2:

    def test(c):
        for value in c:
            print(value.habla())
        print('----------------------------------')

    def test2(c):
        for value in c:
            print(value.habla())
        print('----------------------------------')

    def getParam (elem):
        return elem

    a = Animal(3, 3)
    g = Gato(1, 2)
    lM = LoroMutante(3, 3)

    granja = collections.deque()
    granja.append(a)
    granja.append(g)
    granja.append(lM)
    test(granja)
    test2(granja)
    p = getParam(g)