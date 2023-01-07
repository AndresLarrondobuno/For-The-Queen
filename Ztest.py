import random as rng
from Base_de_Datos import criaturas

class Persona:
    cantidad_de_ojos = 2
    cantidad_de_piernas = 2 #en el mejor de los casos

    def __init__(self, nombre, edad, altura, peso, coeficiente_intelectual):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso= peso
        self.coeficiente_intelectual = coeficiente_intelectual
    
    def __repr__(self):
        return self.nombre
    
    def existir(self):
        print("existo")

persona_uno = Persona('pepe', 20, 1.8, 78, 185)
persona_dos = Persona('pepe', 38, 1.75, 80, 180)
persona_tres = Persona('juan', 38, 1.75, 80, 190)
persona_cuatro = Persona('juan', 38, 1.75, 80, 175)
persona_cinco = Persona('mario', 38, 1.75, 80, 175)
personas = [persona_uno.nombre, persona_dos.nombre, persona_tres.nombre, persona_cuatro.nombre, persona_cinco.nombre]

###


a,b = 2,2

print(a,b)

'''
idea juego de ritmo: control por presion
ej: si le pegas fuerte a la tecla X, es porque viene una nota mas "importante"
'''

        
