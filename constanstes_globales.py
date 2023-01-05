import pygame
import os
import random as rng
from Base_de_Datos import clases
pygame.font.init()


#TAMAÑOS
ANCHO_TABLERO, ALTO_TABLERO = 600, 600
ANCHO_CASILLA, ALTO_CASILLA = int(ANCHO_TABLERO/10), int(ALTO_TABLERO/10)

#VENTANA PPAL
WIN = pygame.display.set_mode((ANCHO_TABLERO, ALTO_TABLERO))

    
#IMAGENES
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (ANCHO_TABLERO, ALTO_TABLERO))
BG2 = pygame.image.load(r"C:\Users\54115\Desktop\python\For The Queen\assets\dc-dngn\floor\cobble_blood1.png")
herrero = pygame.image.load(os.path.join("assets", "dc-mon\holy\paladin.png"))
HERRERO = pygame.transform.scale(herrero, (120,120))
erudito = pygame.image.load(os.path.join("assets", "dc-mon\wizard.png"))
ERUDITO = pygame.transform.scale(erudito, (120,120))
cazador = pygame.image.load(os.path.join("assets", "dc-mon\deep_elf_master_archer.png"))
CAZADOR = pygame.transform.scale(cazador, (120,120))
bardo = pygame.image.load(os.path.join("assets", r"dc-mon\unique\mnoleg.png"))
BARDO = pygame.transform.scale(bardo, (120,120))
PISO = pygame.image.load(os.path.join("assets", r"dc-dngn\floor\rect_gray0.png"))

#FUENTES Y COLORES
FUENTE_BASE =  pygame.font.SysFont("Arialblack", 16)
COLOR_NEGRO = "Black"
COLOR_BLANCO = "White"
COLOR_VERDE = "Green"
COLOR_CELESTE = "lightskyblue"

#TEXTOS PARA LABELS
TEXTO_ELECCION_CLASES = "Bienvenido, porfavor elegi tu clase para comenzar"


#OBJETOS
LISTA_DE_CLASES = list(clases.keys())

#COORDENADAS UTILES
CENTRO_IZQUIERDA_IZQUIERDA = (WIN.get_width()/2 - 250, WIN.get_height()/2)
CENTRO_IZQUIERDA = (WIN.get_width()/2 - 125, WIN.get_height()/2)
CENTRO = (WIN.get_width()/2, WIN.get_height()/2)
CENTRO_DERECHA = (WIN.get_width()/2 + 125, WIN.get_height()/2)

POSICION_INICIAL = (0,0)
