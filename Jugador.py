import random as rng
from Habitante_de_Fahrul import *
from Base_de_Datos import clases
from Seleccionador_de_Aventureros import *

class Jugador:
    def __init__(self, nombre):
        self.id = None
        self.nombre = nombre
        lista_de_clases = list(clases.keys()) #['herrero', 'erudito'...]
        self.aventureros = [Aventurero(rng.choice(lista_de_clases)) for x in range(3)]#instancio un aventurero con una clase al azar
        self.seleccionador_de_aventureros = Seleccionador_de_Aventureros()
        
    def __repr__(self) -> str:
        return self.nombre


