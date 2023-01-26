from Tablero import Tablero
from Jugador import Jugador
from AdministradorDeEventosPygame import *
from AdministradorDeEventosDeFahrul import *
from Azar import *
from Interfaz import *
from SeleccionadorDeAventureros import *
from SeleccionadorDeCriaturas import *


class Partida:
    FPS = 60

    def __init__(self):
        self.tablero = Tablero()
        self.interfaz = Interfaz(self)
        self.administrador_de_eventos_pygame = AdministradorDeEventosPygame(self)
        self.administrador_de_eventos_de_fahrul = AdministradorDeEventosDeFahrul()
        self.seleccionador_de_aventureros = SeleccionadorDeAventureros()
        self.seleccionador_de_criaturas = SeleccionadorDeCriaturas()
        self.jugador = Jugador("Andres")
        self.reloj = pygame.time.Clock()

        self.encendido = True
        self.actualizar_bucle_principal()

        
    def actualizar_bucle_principal(self):
        texto_eleccion_clases = "Bienvenido, porfavor elegi tu clase para comenzar"
        administrador_de_eventos_pygame = self.administrador_de_eventos_pygame

        self.interfaz.ventana_principal.blit(self.interfaz.background, (self.interfaz.posicion_inicial))
        
        
        while self.encendido:

            self.interfaz.reimprimir_fondo()
            self.interfaz.imprimir_pantalla_de_seleccion(self.jugador, texto_eleccion_clases)
                
            for evento in pygame.event.get(): 
                
                administrador_de_eventos_pygame.cerrar(evento)
                administrador_de_eventos_pygame.clase_fue_elegida_con_boton(evento)
                casilla_bajo_mouse_hover = administrador_de_eventos_pygame.get_casilla_bajo_hover(evento)
            
            self.interfaz.resaltar_casilla(casilla_bajo_mouse_hover)


            self.reloj.tick(Partida.FPS)
            pygame.display.update()


    def eleccion_de_clase_realizada(self):
        botones = self.interfaz.botones_de_seleccion_de_clase
        for boton in botones:
            if boton.clickeado:
                return True 
        return False
    

            
        
    
      
partida = Partida()





        




