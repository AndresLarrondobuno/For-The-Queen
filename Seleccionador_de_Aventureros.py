from Habitante_de_Fahrul import *
class Seleccionador_de_Aventureros:
    def __init__(self, combate):
        self.aventureros = None
    
    def agregar_aventureros(self, combate):
        clases_elegidas = combate.jugador.clases_seleccionadas
        for nombre_de_clase in enumerate(clases_elegidas):
            if nombre_de_clase == "herrero":
                clases_elegidas.append(Herrero())
            elif nombre_de_clase == "erudito":
                clases_elegidas.append(Erudito())
            elif nombre_de_clase == "cazador":
                clases_elegidas.append(Cazador())
            elif nombre_de_clase == "bardo":
                clases_elegidas.append(Bardo())

        combate.jugador.aventureros = clases_elegidas

       