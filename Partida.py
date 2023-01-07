from Tablero import Tablero
from Jugador import Jugador
from AdministradorDeEventos import *
from Constanstes_globales import *
from Azar import *
from Interfaz import *


class Partida:
    FPS = 60

    def __init__(self):
        self.tablero = Tablero()
        self.interfaz = Interfaz(self.tablero)
        self.administrador_de_eventos = AdministradorDeEventos()
        self.jugador = Jugador("andres")
        self.reloj = pygame.time.Clock()

        self.encendido = True
        self.actualizar_bucle_principal()

        

    
    
    def actualizar_bucle_principal(self):
            texto_de_usuario = ''
            self.interfaz.ventana_principal.blit(self.interfaz.background, (POSICION_INICIAL))
            #boton_comenzar = Boton("Comenzar", COLOR_BLANCO)
            
        
            while self.encendido:

                self.interfaz.reimprimir_fondo()
                
                if self.interfaz.boton_clickeado():
                    self.interfaz.imprimir_pantalla_de_seleccion(self.jugador, TEXTO_ELECCION_CLASES, self.interfaz.botones_de_seleccion_de_personaje)
                else:
                    self.interfaz.imprimir_tablero(self.tablero)

                for evento in pygame.event.get(): #recorre los eventos ocurridos

                    if evento.type == pygame.QUIT:
                        self.administrador_de_eventos.cerrar(self)#rari, no c porque se me hace que esto puede hacerse de otra forma

                    if evento.type == pygame.KEYDOWN: 
                        if evento.key == pygame.K_BACKSPACE:
                            texto_de_usuario = texto_de_usuario[:-1]
                        else:
                            texto_de_usuario = texto_de_usuario + evento.unicode
                    
                    self.administrador_de_eventos.seleccion_de_personaje(evento, self)#idem↑

                    '''
                    if evento.type == pygame.MOUSEMOTION:
                        if boton_comenzar.mouse_colisiona(posicion_mouse):
                            boton_comenzar.color = (255,0,0)
                        else:
                            boton_comenzar.color = (0,255,0)
                    '''

                self.reloj.tick(Partida.FPS)
                pygame.display.update()

        
partida = Partida()





        




