import random as rng
from Seleccionador_de_Criaturas import *
from Base_de_Datos import *
from Habitante_de_Fahrul import *
from Jugador import *

class Combate:
    def __init__(self, jugador):
        self.aventureros = jugador.aventureros #list
        self.criaturas = Seleccionador_de_Criaturas(self).criaturas
    
    def asignar_dificultad(self):
        niveles_de_aventureros = [aventurero.nivel for aventurero in self.aventureros]
        dificultad_del_combate = round(sum(niveles_de_aventureros)/len(niveles_de_aventureros))
        print(dificultad_del_combate)
    




andres = Jugador("andres")
combate_uno = Combate(andres)

print(combate_uno.aventureros)
print(combate_uno.criaturas)
combate_uno.asignar_dificultad()
for aventurero in combate_uno.aventureros:
    print(type(aventurero))

