from Loro import Loro
class LoroMutante (Loro):
    def __init__(self, patas, ojos):
        super(LoroMutante, self).__init__(patas, ojos)

    def vuela(self):
        return "vuelo ..."
