import pygame

class AdministradorDeEventos:
    
    def __init__(self):
        self.evento = None
    

    def actualizar(self):
        for evento in pygame.event.get(): #recorre los eventos ocurridos
            if evento.type == pygame.QUIT:
                self.cerrar(evento)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                self.seleccion_de_personaje(evento)


    def cerrar(self, partida):
        partida.encendido = False
        pygame.quit()
        exit()
    

    def seleccion_de_personaje(self, evento, partida):
        posicion_mouse = pygame.mouse.get_pos()
        for boton in partida.interfaz.botones_de_seleccion_de_personaje:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton.mouse_colisiona(posicion_mouse) and partida.jugador.aventurero == None:
                    boton.clickeado = True
                    partida.jugador.agregar_aventurero(boton.clase_seleccionada)
                    partida.interfaz.imprimir_tablero(partida.tablero)
                    
