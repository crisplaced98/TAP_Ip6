from abc import ABC, abstractmethod


class Operable(ABC):
    @abstractmethod
    def suma(self, otro):
        pass

    @abstractmethod
    def resta(self, otro):
        pass

    @abstractmethod
    def multiplicacion(self, otro):
        pass

    @abstractmethod
    def division(self, otro):
        pass
