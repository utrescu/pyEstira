__author__ = 'xavier'
from random import randrange


class Jugador(object):

    def __init__(self, nom, image=None,  vida=20):
        self.nom = nom
        self.forca = vida

        self.imatge = image
        self.x = 0
        self.y = 0

    def get_nom(self):
        return self.nom

    def estira(self):
        return randrange(0, self.forca)

    def mou(self, moviment):
        # Mou la imatge
        self.x += moviment

    def posiciona(self, x, y):
        self.x = x
        self.y = y - (self.imatge.get_height()/2)        

    def get_imatge(self):
        return self.imatge

    def get_punt_maxim(self):
        return self.x + self.imatge.get_width()

    def get_posicio(self):
        return self.x, self.y

    def get_ample(self):
        return self.imatge.get_width()

    def __str__(self):
        return "Objecte " + self.nom

    def __unicode__(self):
        return u'Objecte ' + self.nom

    def __repr__(self):
        return "Objecte " + self.nom
