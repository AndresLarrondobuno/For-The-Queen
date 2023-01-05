import random as rng
from Base_de_Datos import criaturas
import pygame
from Interfaz import Boton
from Constanstes_globales import *

class Persona:
    cantidad_de_ojos = 2
    cantidad_de_piernas = 2 #en el mejor de los casos

    def __init__(self, nombre, edad, altura, peso, coeficiente_intelectual):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso= peso
        self.coeficiente_intelectual = coeficiente_intelectual
    
    def __repr__(self):
        return self.nombre
    
    def existir(self):
        print("existo")

persona_uno = Persona('pepe', 20, 1.8, 78, 185)
persona_dos = Persona('pepe', 38, 1.75, 80, 180)
persona_tres = Persona('juan', 38, 1.75, 80, 190)
persona_cuatro = Persona('juan', 38, 1.75, 80, 175)
persona_cinco = Persona('mario', 38, 1.75, 80, 175)
personas = [persona_uno.nombre, persona_dos.nombre, persona_tres.nombre, persona_cuatro.nombre, persona_cinco.nombre]

###
pygame.init()


pygame.display.set_caption("For The Queen")
RAIZ = pygame.display.set_mode((600, 600))
RECTANGULO = pygame.Rect(0,0,20,30)

def bucle():

    encendido = True
    reloj = pygame.time.Clock()
    FPS = 30
    RAIZ.blit(BG, (POSICION_INICIAL))
    boton_comenzar = Boton("Comenzar", COLOR_BLANCO)



    while encendido:
        reloj.tick(FPS)

        if boton_comenzar.clickeado == False:
            print("dibujando")
            boton_comenzar.dibujar(RAIZ)

        for evento in pygame.event.get(): #recorre los eventos ocurridos
            posicion_mouse = pygame.mouse.get_pos()

            if evento.type == pygame.QUIT:
                encendido = False
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_comenzar.mouse_colisiona(posicion_mouse):
                    boton_comenzar.clickeado = True



        pygame.display.update()


    








        
