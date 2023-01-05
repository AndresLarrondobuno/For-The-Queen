import pygame
from Azar import *
from Constanstes_globales import *
from Seleccionador_de_Aventureros import *
from Partida import *


pygame.init()
pygame.display.set_caption("For The Queen")


class Interfaz:

    def __init__(self, tablero):
        self.bucle_principal_de_partida(tablero)
    

    def bucle_principal_de_partida(self, tablero):
        
        def imprimir_tablero():
            for casilla in tablero.casillas:
                WIN.blit(PISO, (casilla.origen_de_dibujo))


        def reimprimir_fondo():
            WIN.blit(BG, (POSICION_INICIAL))

        
        def imprimir_pantalla_de_seleccion(jugador, texto, botones):
            if jugador.aventurero == None:
                superficie_de_texto = FUENTE_BASE.render(texto, True, COLOR_VERDE)
                ancho_de_caja_de_texto, alto_de_caja_de_texto = superficie_de_texto.get_width(), superficie_de_texto.get_height()
                caja_de_texto = pygame.Rect(0,0,ancho_de_caja_de_texto+5,alto_de_caja_de_texto+5)
                #pygame.draw.rect(WIN, COLOR_CELESTE, caja_de_texto, 2)
                
                WIN.blit(superficie_de_texto, (caja_de_texto.x + 5, caja_de_texto.y + 5))

                for boton in botones:
                    boton.dibujar(WIN)
        
        
        def agregar_seleccion_de_personaje_a_tablero(jugador):
            
            if jugador.aventurero == None:
                casilla_inicial = Azar.get_casilla_inicial(tablero.casillas)
                WIN.blit(jugador.aventurero.sprite, casilla_inicial.coordenadas)

                
        
        encendido = True
        reloj = pygame.time.Clock()
        FPS = 60

        contenedor_de_texto_seleccion_de_clases = pygame.Rect(0,0,0,32)
        texto_de_usuario = ''


        #boton_comenzar = Boton("Comenzar", COLOR_BLANCO)
        WIN.blit(BG, (POSICION_INICIAL))
       

        boton_bardo = Boton_con_imagen(BARDO, CENTRO_IZQUIERDA_IZQUIERDA)
        boton_herrero = Boton_con_imagen(HERRERO, CENTRO_IZQUIERDA)
        boton_erudito = Boton_con_imagen(ERUDITO, CENTRO)
        boton_cazador = Boton_con_imagen(CAZADOR, CENTRO_DERECHA)
        botones_de_seleccion_de_personaje = [boton_bardo, boton_herrero, boton_erudito, boton_cazador]
        
        while encendido:
            reimprimir_fondo()
            imprimir_pantalla_de_seleccion(partida.jugador, TEXTO_ELECCION_CLASES, botones_de_seleccion_de_personaje)

            
            for evento in pygame.event.get(): #recorre los eventos ocurridos
                posicion_mouse = pygame.mouse.get_pos()

                if evento.type == pygame.QUIT:
                    encendido = False
                    pygame.quit()
                    exit()

                if evento.type == pygame.KEYDOWN: 
                    if evento.key == pygame.K_BACKSPACE:
                        texto_de_usuario = texto_de_usuario[:-1]
                    else:
                        texto_de_usuario = texto_de_usuario + evento.unicode
                
                for boton in botones_de_seleccion_de_personaje:
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if boton.mouse_colisiona(posicion_mouse) and partida.jugador.aventurero == None:
                            boton.clickeado = True
                            partida.jugador.agregar_aventurero(boton.clase_seleccionada)
                            imprimir_tablero()

                '''
                if evento.type == pygame.MOUSEMOTION:
                    if boton_comenzar.mouse_colisiona(posicion_mouse):
                        boton_comenzar.color = (255,0,0)
                    else:
                        boton_comenzar.color = (0,255,0)
                '''

            reloj.tick(FPS)
            pygame.display.update()




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


interfaz = Interfaz(partida.tablero)

