import pygame

class AdministradorDeEventosPygame:
    
    def __init__(self, partida):
        self.partida = partida
        self.evento = None
    

    def cerrar(self, evento):
        if evento.type == pygame.QUIT:
            self.partida.encendido = False
            pygame.quit()
            exit()
    

    def clase_fue_elegida_con_boton(self, evento):
        if self.partida.eleccion_de_clase_realizada:
            posicion_mouse = pygame.mouse.get_pos()
            botones = self.partida.interfaz.botones_de_seleccion_de_clase
            sprite_resaltador = self.partida.interfaz.spritesDeResaltado.sprites()[0]
            #sprite_resaltador.activar_resaltado()
            
            for boton in botones:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton.rect.collidepoint(posicion_mouse) and self.partida.jugador.aventurero == None:
                        boton.clickeado = True
                        self.partida.seleccionador_de_aventureros.agregar_aventurero(self.partida, boton.clase)
                        self.partida.interfaz.imprimir_tablero()
                        self.partida.interfaz.agregar_personaje_a_tablero()
                    

    def personaje_seleccionado(self, evento):
        if self.partida.jugador.aventurero != None:
            casilla_bajo_hover = self.get_casilla_por_hover()
            casilla_personaje = self.partida.tablero.get_casilla_ocupada()
            personaje_esta_bajo_hover = casilla_bajo_hover is casilla_personaje

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if personaje_esta_bajo_hover and (not casilla_personaje.seleccionada):
                    casilla_personaje.seleccionada = True
                    self.partida.interfaz.resaltar_casilla(casilla_bajo_hover)
                elif personaje_esta_bajo_hover and casilla_personaje.seleccionada:
                    casilla_personaje.seleccionada = False
                    self.partida.interfaz.quitar_resaltado_a_casilla(casilla_bajo_hover)
                

                    
    def get_casilla_bajo_hover(self, evento):
        posicion_mouse = pygame.mouse.get_pos()
        if evento.type == pygame.MOUSEMOTION:
            for casilla in self.partida.tablero.casillas:
                if casilla.rect.collidepoint(posicion_mouse):
                    casilla.bajoHover = True
                    #cuanjdo vuelve a iterar tengo que buscar la casilla falgeada
                    return casilla
    

    def mouse_dentro_del_tablero(self, evento):
        ventana_principal = self.partida.interfaz.ventana_principal
        if evento.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x < 0 or mouse_x > ventana_principal.get_width() or mouse_y < 0 or mouse_y > ventana_principal.get_height():
                return False
            else:
                return True
     

    def resaltar_casilla_por_hover(self, evento):
        if self.partida.eleccion_de_clase_realizada():
            casilla_bajo_hover = self.get_casilla_por_hover(evento)
            tablero = self.partida.tablero

            if self.mouse_dentro_del_tablero(evento):
                tablero.resetear_bajoHover_de_casillas()
                casilla_bajo_hover.bajoHover = True
                self.partida.interfaz.resaltar_casilla(casilla_bajo_hover)
    


    


                



   
    
            
                
                        
                    






                    
