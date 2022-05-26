class Animal:
    def __init__(self, patas, ojos):
        self._patas = patas
        self._ojos = ojos

    def getBicho(bicho):
        return bicho

    @property
    def patas (self, patas):
        self._patas = patas

    @patas.setter
    def patas(self):
        return self._patas

    @property
    def ojos(self, ojos):
        self._ojos = ojos

    @ojos.setter
    def ojos(self):
        return self._ojos

    def habla(self):
        return "Soy un animal"