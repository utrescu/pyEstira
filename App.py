# -*- coding: utf-8 -*-
__author__ = 'xavier'
import pygame
import sys
from Competicio import Competicio
from Jugador import Jugador
from pygame.locals import*

pygame.init()

def start():
    """
    Comença el programa.
    :return:
    """

    # Crea la finestra
    finestra = pygame.display.set_mode((1200, 400))

    # Crear els jugadors i els afegeixo a la competició
    competicio = Competicio(finestra)

    competicio.afegirjugador(0, Jugador("Pep1", pygame.image.load('jugador1.png')))
    competicio.afegirjugador(0, Jugador("Pep2", pygame.image.load('jugador1.png')))
    competicio.afegirjugador(0, Jugador("Pep3", pygame.image.load('jugador1.png')))
    competicio.afegirjugador(0, Jugador("Pep4", pygame.image.load('jugador1.png')))
    competicio.afegirjugador(0, Jugador("Pep5", pygame.image.load('jugador1.png')))
    competicio.afegirjugador(0, Jugador("Pep6", pygame.image.load('jugador1.png')))
    competicio.afegirjugador(0, Jugador("Pep6", pygame.image.load('jugador1.png')))


    competicio.afegirjugador(1, Jugador("Met1", pygame.image.load('jugador2.png')))
    competicio.afegirjugador(1, Jugador("Met2", pygame.image.load('jugador2.png')))
    competicio.afegirjugador(1, Jugador("Met3", pygame.image.load('jugador2.png')))
    competicio.afegirjugador(1, Jugador("Met4", pygame.image.load('jugador2.png')))
    competicio.afegirjugador(1, Jugador("Met5", pygame.image.load('jugador2.png')))
    competicio.afegirjugador(1, Jugador("Met6", pygame.image.load('jugador2.png')))
    competicio.afegirjugador(1, Jugador("Met7", pygame.image.load('jugador2.png')))

    # Posiciona els jugadors
    competicio.ready()

    # Competeixen fins que un dels equips ha estat portat al centre
    while not competicio.acabat():
        finestra.fill((255, 255, 255))

        for events in pygame.event.get():
            if events.type == QUIT:
                pygame.quit()
                sys.exit()

        # Estirada dels dos equips
        competicio.estira()

        # Pinto les imatges
        competicio.pinta()

        pygame.display.flip()
        pygame.time.delay(80)

    pygame.time.delay(3000)


def main():
    start()
    pass

main()
