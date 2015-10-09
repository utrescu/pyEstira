# -*- coding: utf-8 -*-
__author__ = 'xavier'
from random import randrange


class Jugador(object):
    """
    Classe que simula un dels jugadors d'estirar a corda
    """

    def __init__(self, nom, image=None,  forca_maxima=20):
        self.nom = nom
        self.forca = forca_maxima

        self.imatge = image
        self.x = 0
        self.y = 0

    def get_nom(self):
        """
        :return: Retorna el nom del jugador
        """
        return self.nom

    def estira(self):
        """
        :return: retorna la força amb la que estira el jugador
        en un moment donat
        """
        return randrange(0, self.forca)

    def mou(self, moviment):
        """
        Mou la imatge del jugador les posicions especificades
        :param moviment: Quants de píxels s'ha de moure
        :return:
        """
        self.x += moviment

    def posiciona(self, x, y):
        """
        Posiciona el jugador en les coordenades
        :param x: Coordenada X
        :param y: Coordenada Y
        :return:
        """
        self.x = x
        self.y = y - (self.imatge.get_height()/2)        

    def get_imatge(self):
        """
        :return: Retorna la imatge del jugador

        """
        return self.imatge

    def get_punt_maxim(self):
        """
        Es fa servir per pintar-lo a pantalla.
        :return:Retorna el punt més a la dreta del jugador
        """
        return self.x + self.imatge.get_width()

    def get_posicio(self):
        """
        :return: Retorna la posició en la que està el jugador
        """
        return self.x, self.y

    def get_ample(self):
        """
        :return: Retorna l'amplada de la imatge del jugador
        """
        return self.imatge.get_width()

    def __str__(self):
        """
        :return: Representació en text de l'objecte
        """
        return "Objecte " + self.nom

    def __unicode__(self):
      """
      :return: Representació en text de l'objecte
      """
      return u'Objecte ' + self.nom

    def __repr__(self):
        """
        :return:Representació en text de l'objecte
        """
        return "Objecte " + self.nom
