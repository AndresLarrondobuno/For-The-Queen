import pygame
import random as rng
import time
import os
pygame.font.init()

# ventana ppal
ANCHO, ALTO = 1200, 680
WIN = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("For The Queen")

# cargar las imagenes
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (ANCHO, ALTO))


def main():
    run = True
    FPS = 60
    reloj = pygame.time.Clock()
    main_font = pygame.font.SysFont("comicsans", 50)

    def reimprimir_ventana():
        WIN.blit(BG, (0,0))
        pygame.display.update()

    while run:
        reloj.tick(FPS)
        reimprimir_ventana()

        for event in pygame.event.get(): # chequea 60 veces por segundo si algun evento QUIT ocurre
            if event.type == pygame.QUIT:
                run = False

main()
