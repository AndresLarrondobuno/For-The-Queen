import random as rng
from Habitante_de_Fahrul import *
from Seleccionador_de_Aventureros import *

class Jugador:
    def __init__(self, nombre):
        self.id = None
        self.nombre = nombre
        self.aventurero = None
        #self.seleccionador_de_aventureros = Seleccionador_de_Aventureros()



    def __repr__(self) -> str:
        return self.nombre
    

    def agregar_aventurero(self, clase):
        if clase == "herrero":
            self.aventurero = Herrero(clase)
        elif clase == "erudito":
            self.aventurero = Erudito(clase)
        elif clase == "cazador":
            self.aventurero = Cazador(clase)
        elif clase == "bardo":
            self.aventurero = Bardo(clase)



