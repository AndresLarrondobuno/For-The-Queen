from Casilla import *


class Tablero:

    def __init__(self):
        self.alto = 10 #cantidad de casillas
        self.ancho = 10
        self.casillas = self.agregar_casillas()
    
    def agregar_casillas(self):
        casillas = set()
        for x in range(self.ancho):
            for y in range(self.alto):
                casillas.add(Casilla(x,y))
        return casillas


