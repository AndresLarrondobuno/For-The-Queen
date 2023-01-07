from Casilla import *

class Tablero:

    def __init__(self):
        self.ancho = 600
        self.alto = 600
        self.alto_en_casillas = 10 #cantidad de casillas
        self.ancho_en_casillas = 10

        self.casillas = self.agregar_casillas()
        
    
    def agregar_casillas(self):
        casillas = set()
        for x in range(self.ancho_en_casillas):
            for y in range(self.alto_en_casillas):
                casilla = Casilla((x,y), self)
                casillas.add(casilla)
        return casillas


