from calc.Operable import Operable
class PInteger(Operable):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def suma(self, otro):
        return PInteger(self.__valor + otro.valor)

    def resta(self, otro):
        return PInteger(self.__valor - otro.valor)

    def multiplicacion(self, otro):
        return PInteger(self.__valor * otro.valor)

    def division(self, otro):
        return PInteger(self.__valor / otro.valor)

    def __str__(self):
        return '('+ str(self.__valor) + ')'