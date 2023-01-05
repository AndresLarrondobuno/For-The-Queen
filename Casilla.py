

class Casilla:

    ANCHO_TABLERO, ALTO_TABLERO = 600, 600
    ANCHO_CASILLA, ALTO_CASILLA = int(ANCHO_TABLERO/10), int(ALTO_TABLERO/10)


    def __init__(self, coordenadas):
        self.x = coordenadas[0]
        self.y = coordenadas[1]
        self.coordenadas = coordenadas
        self.origen_de_dibujo = (int(self.x*Casilla.ALTO_CASILLA), int(self.y*Casilla.ANCHO_CASILLA))
    
    def __repr__(self) -> str:
        return str((self.x, self.y))




        