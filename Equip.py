# -*- coding: utf-8 -*-
__author__ = 'xavier'


class Equip(object):
    """
    Classe que representa un dels equips d'estirar a corda.

    Conté la llista dels jugadors que en formen part
    """

    def __init__(self, equip):
        self.equip = equip
        self.jugadors = []

    def getnom(self):
        """
        :return: retorna el nom del jugador
        """
        return self.equip

    def afegir_jugador(self, jugador):
        """
        Afegeix un jugador a l'equip
        :param jugador: jugador a afegir
        :return:
        """
        self.jugadors.append(jugador)

    def estira(self):
        """
        Suma les forces de tots els jugadors de l'equip
        :return: suma de les forces
        """
        forca = 0
        for jugador in self.jugadors:
            forca = forca + jugador.estira()
        return forca

    def mou(self, moviment):
        """
        Mou tots els jugadors 'x' pixels
        :param moviment: pixels a moure
        :return:
        """
        for jugador in self.jugadors:
            jugador.mou(moviment)

    def get_jugadors(self):
        """
        :return: llista dels jugadors de l'equip
        """
        return self.jugadors

    @property
    def quants_jugadors(self):
        """
        :return: Número de jugadors de l'equip
        """
        return len(self.jugadors)

    def posiciona_jugadors(self, x, y):
        """
        Posiciona els jugadors en una posició a partir
        de l'especificada
        :param x:
        :param y:
        :return:
        """
        posx = x
        for jugador in self.jugadors:
            jugador.posiciona(posx, y)
            posx = jugador.get_punt_maxim()

        return posx

    def suma_amplades(self):
        """
        Suma les amplades dels jugadors per saber quan d'espai
        ocupa l'equip
        :return: amplada de l'equip
        """
        suma = 0
        for jugador in self.jugadors:
            suma = suma + jugador.get_ample()
        return suma
