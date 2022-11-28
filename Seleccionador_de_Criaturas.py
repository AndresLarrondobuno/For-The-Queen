from Base_de_Datos import *
from Habitante_de_Fahrul import *
from Azar import *
import random as rng

class Seleccionador_de_Criaturas:
    def __init__(self, combate):
        self.criaturas = self.generar_enfrentamiento(combate)

        

    def generar_enfrentamiento(self, combate):
   
        roll = Azar.roll(10)
        if roll:
            criaturas = self.generar_enjambre()
        else:
            criaturas = self.generar_oponente()
        return criaturas
    

    def generar_enjambre(self):
        criatura = rng.choice(criaturas.keys())
        enjambre = [Criatura(criatura) for x in range(3)]
        return enjambre
        
    
    def generar_oponente(self):
        lista_de_criaturas = list(criaturas.keys())
        criatura = Criatura(rng.choice(lista_de_criaturas))
        return criatura

