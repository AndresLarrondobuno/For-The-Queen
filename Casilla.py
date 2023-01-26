import pygame
from pygame import Rect #este import no deberia ser necesario, pero si no lo agrego no puedo acceder a Rect (?)
from Sprites import SpriteParaCasilla

class Casilla:

    def __init__(self, coordenadas, tablero):
        self.ancho = int(tablero.ancho/10)
        self.alto =  int(tablero.alto/10)
        self.x = coordenadas[0]
        self.y = coordenadas[1]
        self.coordenadas = coordenadas
        self.origen_de_dibujo = (int(self.x*self.ancho), int(self.y*self.alto))
        self.rect = Rect(self.origen_de_dibujo[0],self.origen_de_dibujo[1], self.ancho, self.alto)
        self.imagen = pygame.transform.scale(pygame.image.load(r"C:\Users\54115\Desktop\python\For The Queen\assets\dc-dngn\floor\cobble_blood1.png"), (self.ancho, self.alto))
        self.sprite = SpriteParaCasilla(self)

        self.ocupada = False
        self.seleccionada = False
        self.bajoHover = False
    
    def __repr__(self) -> str:
        return str((self.x, self.y))
    

    def casilla_ocupada(self):
        if self.ocupada:
            return self
    

    def casilla_bajo_hover(self):
        if self.bajoHover:
            return self
    

        
    

    




        