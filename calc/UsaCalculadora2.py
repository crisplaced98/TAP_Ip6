from calc.PDouble import PDouble
from calc.PInteger import PInteger
from calc.PVector import PVector
from calc.Calculadora import Calculadora
import collections

class UsaCalculadora2:
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

    v1 = PVector(penteros)

    penteros2 = collections.deque()
    penteros2.append(PInteger(2))
    penteros2.append(PInteger(2))
    penteros2.append(PInteger(2))

    v2 = PVector(penteros2)

    penterosi = collections.deque()
    penterosi.append(PInteger(0))
    penterosi.append(PInteger(0))
    penterosi.append(PInteger(0))

    v3 = PVector(pdoubles)

    pdoubles2 = collections.deque()
    pdoubles2.append(PDouble(2.0))
    pdoubles2.append(PDouble(2.0))
    pdoubles2.append(PDouble(2.0))

    v4 = PVector(pdoubles2)

    pdoublesi = collections.deque()
    pdoublesi.append(PDouble(0.0))
    pdoublesi.append(PDouble(0.0))
    pdoublesi.append(PDouble(0.0))

    vectorintinicial = PVector(penterosi)
    vectordoubleinicial = PVector (pdoublesi)

    vectoresint = collections.deque()
    vectoresint.append(v1)
    vectoresint.append(v2)

    vectoresdouble = collections.deque()
    vectoresdouble.append(v3)
    vectoresdouble.append(v4)

    print(Calculadora.Calcula(penteros, pinicial))
    print(Calculadora.Calcula(pdoubles, pinicial2))
    print(Calculadora.Calcula(vectoresint, vectorintinicial))
    print(Calculadora.Calcula(vectoresdouble, vectordoubleinicial))