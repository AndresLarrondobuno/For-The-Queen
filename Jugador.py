from HabitanteDeFahrul import *
from SeleccionadorDeAventureros import *
from Azar import *

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.aventurero = None


    def __repr__(self) -> str:
        return self.nombre
    

    def mover_aventurero(self):
        casillas_a_recorrer = Azar.roll_de_movimiento(self.aventurero)
        
        
    

    



