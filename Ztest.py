import pygame
from pygame import Rect

pygame.init()

class SpriteParaResaltador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = None
        self.image = None
    
    def update(self, superficie, casilla):
        pygame.draw.rect(superficie, "Green", casilla.rect, 2)


class SpriteParaCasilla(pygame.sprite.Sprite):
    def __init__(self, casilla):
        super().__init__()
        self.origen_de_dibujo = casilla.origen_de_dibujo
        self.image = casilla.imagen
        self.rect = casilla.rect
        self.rect.x = casilla.origen_de_dibujo[0]
        self.rect.y = casilla.origen_de_dibujo[1]


class Tablero():
    def __init__(self):
        self.ancho = 600
        self.alto = 600
        self.alto_en_casillas = 10 #cantidad de casillas
        self.ancho_en_casillas = 10

        self.casillas = self.agregar_casillas()
        
    
    def agregar_casillas(self):
        casillas = set()
        for x in range(self.ancho_en_casillas):
            for y in range(self.alto_en_casillas):
                casilla = Casilla((x,y))
                casillas.add(casilla)
        return casillas


class Casilla:
    def __init__(self, coordenadas):
        self.ancho, self.alto = 60, 60
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


def dibujar_tablero(sprite_group_casillas, superficie):
    sprite_group_casillas.draw(superficie)


def casilla_bajo_hover(evento, posicion_mouse):
    if evento.type == pygame.MOUSEMOTION:
        for casilla in tablero.casillas:
            if casilla.rect.collidepoint(posicion_mouse):
                return casilla
        
        


def resaltar_casilla(ventana_principal, sprite_group_resaltador, casilla_bajo_hover):
    #asignar atributos rect y image al sprite_resaltador usando atributos del objeto casilla
    sprite_resaltador = sprite_group_resaltador.sprites()[0]
    if casilla_bajo_hover != None:
        sprite_resaltador.rect = casilla_bajo_hover.rect
        sprite_resaltador.image = casilla_bajo_hover.imagen
        sprite_group_resaltador.update(ventana_principal, casilla_bajo_hover)
        #pygame.draw.rect(ventana_principal, "Green", casilla.rect, 2)



tablero = Tablero()
reloj = pygame.time.Clock()

sprites_para_casillas = [SpriteParaCasilla(casilla) for casilla in tablero.casillas]
sprite_group_casillas = pygame.sprite.Group(sprites_para_casillas)

sprite_resaltador = SpriteParaResaltador()
sprite_group_resaltador = pygame.sprite.Group(sprite_resaltador)

ventana_principal = pygame.display.set_mode((600, 600))

imagen_para_casillas = pygame.transform.scale(pygame.image.load(r"C:\Users\54115\Desktop\python\For The Queen\assets\dc-dngn\floor\cobble_blood1.png"), (60, 60))


running = True
ultima_casilla_bajo_hover = None

while running:
    posicion_mouse = pygame.mouse.get_pos()
    
    dibujar_tablero(sprite_group_casillas, ventana_principal)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

        casilla_a_resaltar = casilla_bajo_hover(evento, posicion_mouse)
    resaltar_casilla(ventana_principal, sprite_group_resaltador, casilla_a_resaltar)
        

        
    reloj.tick(60)
    pygame.display.update()

pygame.quit()


###




'''
idea juego de ritmo: control por presion
ej: si le pegas fuerte a la tecla X, es porque viene una nota mas "importante"
'''
