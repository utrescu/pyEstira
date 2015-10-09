__author__ = 'xavier'


class Corda(object):

    def __init__(self, image):
        self.x = 0
        self.y = 0
        self.imatge = image

        self.rectangle = (0, 0, 0, 0)

    def posiciona_mocador(self, x, y):
        self.x = x
        self.y = y

    def mou(self, moviment):
        # Mou la imatge
        self.x += moviment
        self.rectangle = (self.rectangle[0] + moviment,
                          self.rectangle[1],
                          self.rectangle[2],
                          self.rectangle[3])

    def get_imatge_mocador(self):
        return self.imatge

    def get_posicio(self):
        return self.x, self.y

    def get_corda(self):
        return self.rectangle

    def set_corda(self, rectangle):
        self.rectangle = rectangle
