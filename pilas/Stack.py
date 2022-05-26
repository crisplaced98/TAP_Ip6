from abc import ABC, abstractmethod
from collections.abc import Iterable


class Stack(ABC, Iterable):
    @abstractmethod
    def push(self, elem):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def llena(self):
        pass

    @abstractmethod
    def vacia(self):
        pass
