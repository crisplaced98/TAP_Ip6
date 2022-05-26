from calc.Operable import Operable
import collections


class PVector(Operable):
    def __init__(self, valores):
        self.__valores = valores

    def suma(self, otro):
        result = collections.deque()
        listotro = otro.valores
        for elem in self.__valores:
            result.append(elem.suma(listotro[self.__valores.index(elem)]))

        return PVector(result)

    def resta(self, otro):
        return None

    def multiplicacion(self, otro):
        return None

    def division(self, otro):
        return None

    @property
    def valores(self):
        return self.__valores

    @valores.setter
    def valores(self, valores):
        self.__valores = valores

    def __str__(self):
        result = '('
        for elem in self.__valores:
            result = result + str(elem) + ' '

        result = result + ')'
        return result
