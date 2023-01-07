import pygame
from Azar import *
from Constanstes_globales import *
from Seleccionador_de_Aventureros import *

pygame.init()
pygame.display.set_caption("For The Queen")


class Interfaz:

    def __init__(self, tablero):
        self.ventana_principal = pygame.display.set_mode((tablero.ancho, tablero.alto))
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (ANCHO_TABLERO, ALTO_TABLERO))

        boton_bardo = Boton_con_imagen(BARDO, CENTRO_IZQUIERDA_IZQUIERDA)
        boton_herrero = Boton_con_imagen(HERRERO, CENTRO_IZQUIERDA)
        boton_erudito = Boton_con_imagen(ERUDITO, CENTRO)
        boton_cazador = Boton_con_imagen(CAZADOR, CENTRO_DERECHA)
        self.botones_de_seleccion_de_personaje = [boton_bardo, boton_herrero, boton_erudito, boton_cazador]
    

    def boton_clickeado(self):
        for boton in self.botones_de_seleccion_de_personaje:
            if boton.clickeado:
                return True
          


    def imprimir_tablero(self, tablero):
        for casilla in tablero.casillas:
            self.ventana_principal.blit(PISO, (casilla.origen_de_dibujo))
    

    def reimprimir_fondo(self):
        self.ventana_principal.blit(self.background, (POSICION_INICIAL))
    

    def imprimir_pantalla_de_seleccion(self, jugador, texto, botones):
        if jugador.aventurero == None:
            superficie_de_texto = FUENTE_BASE.render(texto, True, COLOR_VERDE)
            ancho_de_caja_de_texto, alto_de_caja_de_texto = superficie_de_texto.get_width(), superficie_de_texto.get_height()
            caja_de_texto = pygame.Rect(0,0,ancho_de_caja_de_texto+5,alto_de_caja_de_texto+5)
            
            self.background.blit(superficie_de_texto, (caja_de_texto.x + 5, caja_de_texto.y + 5))

            for boton in botones:
                boton.dibujar(self.background)

    
    def agregar_seleccion_de_personaje_a_tablero(self):
        if self.jugador.aventurero == None:
            casilla_inicial = Azar.get_casilla_inicial(self.partida.tablero.casillas)
            self.background.blit(self.jugador.aventurero.sprite, casilla_inicial.coordenadas)



        
        
 

                





class Boton_con_imagen:
    def __init__(self, imagen, coordenadas):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.topleft = coordenadas
        self.x, self.y = coordenadas[0], coordenadas[1]
        self.rect_borde = pygame.draw.rect(WIN, "Green", self.rect, 3)
        self.ancho = imagen.get_width()
        self.alto = imagen.get_height()
        self.clickeado = False
        self.clase_seleccionada = None
        self.asignar_clase()
    

    def __repr__(self) -> str:
        return self.clase_seleccionada
    

    def asignar_clase(self):
        if self.imagen == HERRERO:
            self.clase_seleccionada = "herrero"
        elif self.imagen == ERUDITO:
            self.clase_seleccionada = "erudito"
        elif self.imagen == CAZADOR:
            self.clase_seleccionada = "cazador"
        elif self.imagen == BARDO:
            self.clase_seleccionada = "bardo"


    def dibujar(self, superficie):
       superficie.blit(self.imagen, (self.rect.x, self.rect.y))
    

    def mouse_colisiona(self, posicion):
        if (posicion[0] > self.x and posicion[0] < self.x + self.ancho) and (posicion[1] > self.y and posicion[1] < self.y + self.alto):
            return True
        return False




class Boton:
    def __init__(self, texto, color, x=CENTRO[0], y=CENTRO[1], alto=120, ancho=70):
        self.texto = texto
        self.color = color
        self.x = x 
        self.y = y 
        self.ancho = alto
        self.alto = ancho
        self.origen = (x, y)
        self.clickeado = False


    def dibujar(self, superficie):
        pygame.draw.rect(superficie, self.color,(self.x, self.y, self.ancho, self.alto),0)
        font = FUENTE_BASE
        text = font.render(self.texto, 1, (0,0,0))
        superficie.blit(text, (self.x + (self.ancho/2 - text.get_width()/2), self.y + (self.alto/2 - text.get_height()/2)))
        
    
    def mouse_colisiona(self, posicion):
        if (posicion[0] > self.x and posicion[0] < self.x + self.ancho) and (posicion[1] > self.y and posicion[1] < self.y + self.alto):
            return True
        return False



