from calc.PInteger import PInteger
from calc.PDouble import PDouble
from calc.Calculadora import Calculadora
import collections


class UsaCalculadora:
    penteros = collections.deque()
    penteros.append(PInteger(1))
    penteros.append(PInteger(7))
    penteros.append(PInteger(8))

    pdoubles = collections.deque()
    pdoubles.append(PDouble(1.5))
    pdoubles.append(PDouble(7.3))
    pdoubles.append(PDouble(8.8))

    pinicial = PInteger(0)
    pinicial2 = PDouble(0.0)

    print(Calculadora.Calcula(penteros, pinicial))
    print(Calculadora.Calcula(pdoubles, pinicial2))
