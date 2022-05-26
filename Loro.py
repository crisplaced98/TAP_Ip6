from Animal import Animal


class Loro(Animal):
    def __init__(self, patas, ojos):
        super().__init__(patas, ojos)

    def habla(self):
        return "Soy un Loro y " + str(super().habla())
