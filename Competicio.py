# -*- coding: utf-8 -*-
from __future__ import division
__author__ = 'xavier'
import pygame
from Equip import Equip
from Corda import Corda


class Competicio(object):
    """
    Objecte que simula l'estirament de corda entre dos equips.

    Mira la força que fa cada un dels equips i els mou coherentment
    segons el resultat obtingut.
    """

    SEPARACIO = 200

    def __init__(self, pantalla, debug=False):
        self.pantalla = pantalla
        self.equips = []
        self.mocador = Corda(pygame.image.load('mocador.png'))
        self.equips.append(Equip('esquerra'))
        self.equips.append(Equip('dret'))
        self.desplasament = 0
        self.DEBUG = debug

    def afegirjugador(self, on, jugador):
        """
        Afegeix un jugador a un dels equips
        :param on: Quin dels equips és
        :param jugador: Jugador a afegir
        :return:
        """
        self.equips[on].afegir_jugador(jugador)

    def ready(self):
        """
        Posiciona els jugadors en la pantalla. Per fer-ho es basa en
        que cada equip indicarà quant d'espai ocupa.
        :return:
        """
        # Posiciona els jugadors
        self.desplasament = 0
        posicio_mocador = 0

        llargada_corda = self.ampladaequips() + self.SEPARACIO * 2

        inici_y = self.pantalla.get_height() / 2

        inici_x = (self.pantalla.get_width() - llargada_corda) / 2
        posx = inici_x
        index = 0
        for equip in self.equips:

            pos = equip.posiciona_jugadors(posx, inici_y)
            posx = pos + self.SEPARACIO
            if index == 0:
                posicio_mocador = posx
                index += 1
            posx += self.SEPARACIO

        self.mocador.set_corda((inici_x - 10, inici_y - 3, llargada_corda + 10, 3))
        self.mocador.posiciona_mocador(posicio_mocador, inici_y)

    def ampladaequips(self):
        """
        :return: Calcula la suma de l'espai que ocupen els dos equips
        """         
        return sum( [equip.suma_amplades() for equip in self.equips] )

    def estira(self):
        """
        Els dos equips estiren i acaben movent-se en una
        direcció segons el que faci més força.
        :return:
        """
        # Obtenir els valors de forca
        forca_esquerra = self.equips[0].estira()
        forca_dreta = self.equips[1].estira()

        pondera = min(self.equips[0].quants_jugadors, self.equips[1].quants_jugadors)

        moviment = (forca_dreta - forca_esquerra) / pondera

        # Moure el mocador i la corda
        self.mocador.mou(moviment)

        # Moure els equips
        for equip in self.equips:
            equip.mou(moviment)

        # Index de desplaçament acumulat
        self.desplasament = self.desplasament + moviment

        if self.DEBUG:
            print("ESQUERRA:" + str(forca_esquerra) + " vs " + "DRETA:" + str(forca_dreta) +
                  " (" + str(moviment) + ") ->" + str(self.desplasament))

    def pinta(self):
        """
        Pinta tot el que fa referència a la pantalla:
          * ratlla del mig
          * Corda i mocador
          * Equips
        :return: res
        """
        # Pinto la ratlla
        mig = self.pantalla.get_width() / 2
        pygame.draw.line(self.pantalla, (0, 0, 0), (mig, 0), (mig, self.pantalla.get_height()))
        # Pinto la corda i el mocador
        pygame.draw.rect(self.pantalla, (255, 255, 0), self.mocador.get_corda())
        self.pantalla.blit(self.mocador.get_imatge_mocador(), self.mocador.get_posicio())

        for equip in self.equips:
            self.pinta_equip(equip)

    def pinta_equip(self, equip):
        """
        Pinta un equip determinat.
        :param equip: equip a pintar
        :return: res
        """
        for jugador in equip.get_jugadors():
            self.pantalla.blit(jugador.get_imatge(), jugador.get_posicio())

    def acabat(self):
        return abs(self.desplasament) > self.SEPARACIO
