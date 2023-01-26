import pygame
from Sprites import *

class BotonConImagen:
    def __init__(self, imagen, clase, coordenadas):
        
        self.imagen = imagen
        self.clase = clase
        self.rect = self.imagen.get_rect()
        self.rect.topleft = coordenadas
        self.x, self.y = coordenadas[0], coordenadas[1]
        self.ancho = self.imagen.get_width()
        self.alto = self.imagen.get_height()

        self.clickeado = False

    
    def __repr__(self) -> str:
        return self.clase
    

    def dibujar(self, superficie):
       superficie.blit(self.imagen, (self.rect.x, self.rect.y))