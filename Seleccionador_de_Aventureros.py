from Habitante_de_Fahrul import *

class Seleccionador_de_Aventureros:
    def __init__(self, combate):
        self.aventurero = None
        self.combate = combate
    
    def agregar_aventurero(self, jugador):

        for nombre_de_clase in jugador.clases_seleccionadas:
            if nombre_de_clase == "herrero":
                jugador.aventurero = Herrero(nombre_de_clase)
            elif nombre_de_clase == "erudito":
                jugador.aventurero = Erudito(nombre_de_clase)
            elif nombre_de_clase == "cazador":
                jugador.aventurero = Cazador(nombre_de_clase)
            elif nombre_de_clase == "bardo":
                jugador.aventurero = Bardo(nombre_de_clase)

        

       