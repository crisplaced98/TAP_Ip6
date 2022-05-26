from pilas.Stack import Stack
from collections.abc import Iterator

class VectorStack(Stack):
    def __init__(self, max):
        self.__monton = []
        self.__max = max
        self.__cnt = 0

    def push(self, elem):
        self.__monton.append(elem)
        self.__cnt += 1

    def pop(self):
        elem = self.__monton.pop()
        self.__cnt -= 1
        return int(elem)

    def llena(self):
        return self.__max == self.__cnt

    def vacia(self):
        return self.__cnt == 0

    def __iter__(self):
        return self.__monton.__iter__()