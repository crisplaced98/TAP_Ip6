from Animal import Animal


class Gato(Animal):
    def __init__(self, patas, ojos):
        super().__init__(patas, ojos)

    def habla(self):
        return "Soy un Gato"
