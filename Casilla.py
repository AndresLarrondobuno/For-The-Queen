

class Casilla:

    def __init__(self, coordenadas, tablero):
        self.ancho = int(tablero.ancho/10)
        self.alto =  int(tablero.alto/10)
        self.x = coordenadas[0]
        self.y = coordenadas[1]
        self.coordenadas = coordenadas
        self.origen_de_dibujo = (int(self.x*self.alto), int(self.y*self.ancho))
    
    
    def __repr__(self) -> str:
        return str((self.x, self.y))




        