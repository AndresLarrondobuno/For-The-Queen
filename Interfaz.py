import pygame
import os
from Azar import *
from SeleccionadorDeAventureros import *
from Sprites import SpriteParaAventurero, SpriteParaBoton, SpriteParaResaltador
from BotonConImagen import BotonConImagen

pygame.init()
pygame.display.set_caption("For The Queen")


class Interfaz:

    def __init__(self, partida):
        self.partida = partida
        self.posicion_inicial = (0,0)
        self.fuente_base = pygame.font.SysFont("Arialblack", 16)
        self.ventana_principal = pygame.display.set_mode((partida.tablero.ancho, partida.tablero.alto))
        self.background = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background.jpg")), (partida.tablero.ancho, partida.tablero.alto))
        self.imagenes_de_aventureros = self.cargar_imagenes_de_aventureros()

        self.botones_de_seleccion_de_clase = self.botones_para_seleccion_de_personaje(self.imagenes_de_aventureros)
        self.sprites_para_casillas = self.sprite_group_casillas()
        self.spritesDeResaltado = pygame.sprite.Group(SpriteParaResaltador())



    def imprimir_tablero(self):
        self.sprites_para_casillas.draw(self.background)
            
            
    def reimprimir_fondo(self):
        self.ventana_principal.blit(self.background, self.posicion_inicial)
    

    def imprimir_pantalla_de_seleccion(self, jugador, texto="Elegi la clase de tu personaje"):
        if not self.partida.eleccion_de_clase_realizada():
            if jugador.aventurero == None:
                superficie_de_texto = self.fuente_base.render(texto, True, "Green")
                ancho_de_caja_de_texto, alto_de_caja_de_texto = superficie_de_texto.get_width(), superficie_de_texto.get_height()
                caja_de_texto = pygame.Rect(0,0,ancho_de_caja_de_texto+5,alto_de_caja_de_texto+5)
                
                self.ventana_principal.blit(superficie_de_texto, (caja_de_texto.x + 5, caja_de_texto.y + 5))

                for boton in self.botones_de_seleccion_de_clase:
                    boton.dibujar(self.ventana_principal)

    
    def agregar_personaje_a_tablero(self):
        casilla_inicial = self.partida.jugador.aventurero.casilla_inicial
        if self.partida.jugador.aventurero != None:
            self.background.blit(self.partida.jugador.aventurero.sprite.image, casilla_inicial.origen_de_dibujo)


    
    def resaltar_casilla(self, casilla_bajo_hover):
        #asignar atributos rect y image al sprite_resaltador usando atributos del objeto casilla
        if self.partida.eleccion_de_clase_realizada():
            sprite_resaltador = self.spritesDeResaltado.sprites()[0]
            if casilla_bajo_hover != None:
                sprite_resaltador.rect = casilla_bajo_hover.rect
                sprite_resaltador.image = casilla_bajo_hover.imagen
                self.spritesDeResaltado.update(self.ventana_principal, casilla_bajo_hover)


    def cargar_imagenes_de_aventureros(self):
        imagen_herrero = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dc-mon\holy\paladin.png")), (120,120))
        imagen_erudito = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dc-mon\wizard.png")), (120,120))
        imagen_cazador = pygame.transform.scale(pygame.image.load(os.path.join("assets", "dc-mon\deep_elf_master_archer.png")), (120,120))
        imagen_bardo = pygame.transform.scale(pygame.image.load(os.path.join("assets", r"dc-mon\unique\mnoleg.png")), (120,120))
        imagenes = {"herrero":imagen_herrero, "erudito":imagen_erudito, "cazador":imagen_cazador, "bardo":imagen_bardo}

        return imagenes
    
    
    def sprite_group_casillas(self):
        casillas = self.partida.tablero.casillas
        sprites_casillas = pygame.sprite.Group()

        for casilla in casillas:
            sprites_casillas.add(casilla.sprite)
            
        return sprites_casillas


    def sprites_aventureros(self):
        grupo = pygame.sprite.Group()
        for imagen in self.imagenes_de_aventureros.values():
            sprite = SpriteParaAventurero(imagen)
            grupo.add(sprite)
        return grupo
            
     
    def botones_para_seleccion_de_personaje(self, imagenes_para_botones):
        coordenadas_bardo = (self.ventana_principal.get_width()/2 - 250, self.ventana_principal.get_height()/2)
        coordenadas_herrero = (self.ventana_principal.get_width()/2 - 125, self.ventana_principal.get_height()/2)
        coordenadas_erudito = (self.ventana_principal.get_width()/2, self.ventana_principal.get_height()/2)
        coordenadas_cazador = (self.ventana_principal.get_width()/2 + 125, self.ventana_principal.get_height()/2)

        boton_bardo = BotonConImagen(imagenes_para_botones["herrero"], "herrero",  coordenadas_bardo)
        boton_herrero = BotonConImagen(imagenes_para_botones["erudito"], "erudito", coordenadas_herrero)
        boton_erudito = BotonConImagen(imagenes_para_botones["cazador"], "cazador", coordenadas_erudito)
        boton_cazador = BotonConImagen(imagenes_para_botones["bardo"], "bardo", coordenadas_cazador)

        botones = [boton_bardo, boton_herrero, boton_erudito, boton_cazador]

        return botones

    



            
   


