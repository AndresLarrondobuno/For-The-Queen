from HabitanteDeFahrul import *

class SeleccionadorDeAventureros:
    def __init__(self):
        pass

 

    def agregar_aventurero(self, partida, clase):
        if clase == "herrero":
            partida.jugador.aventurero = Herrero(clase)
        elif clase == "erudito":
            partida.jugador.aventurero = Erudito(clase)
        elif clase == "cazador":
            partida.jugador.aventurero = Cazador(clase)
        elif clase == "bardo":
            partida.jugador.aventurero = Bardo(clase)

        casilla_inicial = Azar.casilla_al_azar(partida.tablero.casillas)
        casilla_inicial.ocupada = True

        partida.jugador.aventurero.casilla_inicial = casilla_inicial
        partida.jugador.aventurero.posicion = casilla_inicial
    
    

        

       