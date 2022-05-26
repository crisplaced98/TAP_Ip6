class Calculadora:
    def Calcula (valores, inicial):
        result = inicial
        for elem in valores:
            result = result.suma(elem)

        return result