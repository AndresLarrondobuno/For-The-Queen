from Casilla import *

class Tablero:

    def __init__(self):
        self.ancho = 600
        self.alto = 600
        self.alto_en_casillas = 10 #cantidad de casillas
        self.ancho_en_casillas = 10

        self.casillas = self.agregar_casillas()
        self.ultima_casilla_bajo_mouse_hover = None
        
    
    def agregar_casillas(self):
        casillas = set()
        for x in range(self.ancho_en_casillas):
            for y in range(self.alto_en_casillas):
                casilla = Casilla((x,y), self)
                casillas.add(casilla)
        return casillas
    

    def get_ultima_casilla_bajo_mouse_hover(self):
        #conseguir la casilla flageada
        for casilla in self.casillas:
            if casilla.bajoHover:
                return casilla


    def resetear_bajoHover_de_casillas(self):
        for casilla in self.casillas:
            casilla.bajoHover = False
    

    def get_casilla_bajo_hover_por_atributo(self):
        for casilla in self.casillas:
            if casilla.bajoHover == True:
                return casilla
    

    def get_casilla_ocupada(self):
        for casilla in self.casillas:
            if casilla.ocupada:
                return casilla
    

    def test_hover(self):
        contador = 0
        for casilla in self.casillas:
            if casilla.bajoHover == True:
                contador += 1
        print(contador)


    




    

    


