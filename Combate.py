import random as rng
from SeleccionadorDeCriaturas import *
from Base_de_Datos import *
from HabitanteDeFahrul import *
from Jugador import *

class Combate:
    def __init__(self, jugador):
        self.aventurero = jugador.aventurero
        self.criaturas = None
    
    
    def asignar_dificultad(self):
        niveles_de_aventureros = [aventurero.nivel for aventurero in self.aventureros]
        dificultad_del_combate = round(sum(niveles_de_aventureros)/len(niveles_de_aventureros))
        print(dificultad_del_combate)
    





