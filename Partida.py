import pygame
import random as rng
from Tablero import *
from constanstes_globales import *

pygame.font.init()
class Partida:
    #sprites
    sprites = [] #faltan agregar
    sprites_piso = []

    def __init__(self):
        self.tablero = Tablero()
        
 

        #ventana ppal
        self.main()     
        pygame.display.set_caption("For The Queen")
        

    def main(self):
        def reimprimir_ventana():
            WIN.blit(BG, (POSICION_INICIAL))
            for casilla in self.tablero.casillas:
                WIN.blit(PISO, (casilla.origen_de_dibujo))
            pygame.display.update()

        run = True
        FPS = 60
        reloj = pygame.time.Clock()
        main_font = pygame.font.SysFont("comicsans", 50)

        while run:
            reloj.tick(FPS)
            reimprimir_ventana()

            for event in pygame.event.get(): # chequea 60 veces por segundo si algun evento QUIT ocurre
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()                                #true si esa posicion esta dentro del rect
                    sprites_clikeadas = [sprite for sprite in Partida.sprites if sprite.rect.collidepoint(pos)]#sprites bajo el mouse en este frame
                #intentar moverme hasta la casilla correspondiente

partida = Partida()

