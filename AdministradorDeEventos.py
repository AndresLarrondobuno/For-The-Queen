import pygame

class AdministradorDeEventos:
    
    def __init__(self):
        self.evento = None
    

    def detectar_eventos(self):
        for evento in pygame.event.get(): #recorre los eventos ocurridos
            posicion_mouse = pygame.mouse.get_pos()
            self.cerrar(evento)
            self.seleccion_de_personaje(evento, posicion_mouse)


    def cerrar(self, evento):
        if evento.type == pygame.QUIT:
            encendido = False
            pygame.quit()
            exit()
    

    def seleccion_de_personaje(self, evento, posicion_mouse):
        for boton in botones_de_seleccion_de_personaje:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton.mouse_colisiona(posicion_mouse) and partida.jugador.aventurero == None:
                    boton.clickeado = True
                    partida.jugador.agregar_aventurero(boton.clase_seleccionada)
                    imprimir_tablero()
