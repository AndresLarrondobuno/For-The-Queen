from constanstes_globales import ALTO_CASILLA, ANCHO_CASILLA

class Casilla:
    def __init__(self, coordenada_x, coordenada_y):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.origen_de_dibujo = (int(coordenada_x*ALTO_CASILLA), int(coordenada_y*ANCHO_CASILLA))
    
    def __repr__(self) -> str:
        return self.coordenada_x, self.coordenada_y




        