import pygame
import os
import random as rng


ANCHO, ALTO = 600, 600
ANCHO_CASILLA, ALTO_CASILLA = ANCHO/10, ALTO/10
POSICION_INICIAL = (0,0)
    
#cargo las imagenes 
WIN = pygame.display.set_mode((ANCHO, ALTO))
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (ANCHO, ALTO))
HERRERO = pygame.image.load(os.path.join("assets", "dc-mon\holy\paladin.png"))
ERUDITO = pygame.image.load(os.path.join("assets", "dc-mon\wizard.png"))
CAZADOR = pygame.image.load(os.path.join("assets", "dc-mon\deep_elf_master_archer.png"))
BARDO = pygame.image.load(os.path.join("assets", r"dc-mon\unique\mnoleg.png"))
PISO = pygame.image.load(os.path.join("assets", r"dc-dngn\floor\rect_gray0.png"))

