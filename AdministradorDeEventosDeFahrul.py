from Azar import *

class AdministradorDeEventosDeFahrul:
    def __init__(self):
        self.eventos_visibles = []
        self.eventos_no_visibles = []
    

    def agregar_evento(self, evento):
        if evento.visible == True:
            self.eventos_visibles.append(evento)
        elif evento.visible == False:
            self.eventos_no_visibles.append(evento)
    

    def agregar_eventos_de_tablero(self):
        pool_eventos_positivos = 4
        pool_eventos_negativos = 5
        pool_tiendas = 1
        casilla_inicial = Azar.get_casilla_inicial(self.tablero.casillas)
        for evento in range(pool_eventos_positivos):
            evento.agregar_evento()