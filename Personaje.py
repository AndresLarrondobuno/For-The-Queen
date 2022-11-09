from Base_de_Datos import *
from Azar import *
class Personaje:
    vida_base = 25
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.inventario = []
        self.equipables = {'arma':None, 'escudo':None, 'cabeza':None, 'cuello':None, 'torso y piernas':None, 'botas':None }

        self.vitalidad = None
        self.fuerza = None
        self.inteligencia = None
        self.velocidad = None
        self.talento = None
        self.observacion = None
        self.suerte = None


        self.armadura = None
        self.resistencia = None
        self.evasion = None
        self.puntos_de_enfoque = None
        self.puntos_de_movimiento_maximo = 5

    def aplicar_bonuses_de_stats(self):
        if self.fuerza > 50:
            self.armadura += 1
        if self.inteligencia > 50:
            self.resistencia += 1

    
    def atacar(self, *rolls):
        pass
    
    def moverse(self):
        puntos_de_movimiento = Azar.rollear_dados(self.velocidad, 5)
        #incrementar/decrementar posicion en la grilla segun donde clikea el jugador
        
        

class Herrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.habilidad_pasiva = clases["herrero"]["habilidad_pasiva"]
        self.vitalidad = clases["herrero"]["atributos"]["vitalidad"]
        self.fuerza = clases["herrero"]["atributos"]["fuerza"]
        self.inteligencia = clases["herrero"]["atributos"]["inteligencia"]
        self.velocidad = clases["herrero"]["atributos"]["velocidad"]
        self.talento = clases["herrero"]["atributos"]["talento"]
        self.observacion = clases["herrero"]["atributos"]["observacion"]
        self.puntos_de_enfoque = clases["herrero"]["atributos"]["puntos_de_enfoque"]
        self.suerte = clases["herrero"]["atributos"]["vitalidad"]
        self.puntos_de_vida = int( self.vida_base + self.nivel + (0.10*self.nivel*self.vitalidad) + 5)
        self.aplicar_bonuses_de_stats()

class Erudito(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)   
        self.habilidad_pasiva = clases["erudito"]["habilidad_pasiva"]
        self.vitalidad = clases["erudito"]["atributos"]["vitalidad"]
        self.fuerza = clases["erudito"]["atributos"]["fuerza"]
        self.inteligencia = clases["erudito"]["atributos"]["inteligencia"]
        self.velocidad = clases["erudito"]["atributos"]["velocidad"]
        self.talento = clases["erudito"]["atributos"]["talento"]
        self.observacion = clases["erudito"]["atributos"]["observacion"]
        self.puntos_de_enfoque = clases["erudito"]["atributos"]["puntos_de_enfoque"]
        self.suerte = clases["erudito"]["atributos"]["vitalidad"]
        self.puntos_de_vida = int( self.vida_base + self.nivel + (0.10*self.nivel*self.vitalidad) )
        self.aplicar_bonuses_de_stats()

class Cazador(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.habilidad_pasiva = clases["cazador"]["habilidad_pasiva"]
        self.vitalidad = clases["cazador"]["atributos"]["vitalidad"]
        self.fuerza = clases["cazador"]["atributos"]["fuerza"]
        self.inteligencia = clases["cazador"]["atributos"]["inteligencia"]
        self.velocidad = clases["cazador"]["atributos"]["velocidad"]
        self.talento = clases["cazador"]["atributos"]["talento"]
        self.observacion = clases["cazador"]["atributos"]["observacion"]
        self.puntos_de_enfoque = clases["cazador"]["atributos"]["puntos_de_enfoque"]
        self.suerte = clases["cazador"]["atributos"]["vitalidad"]
        self.puntos_de_vida = int( self.vida_base + self.nivel + (0.10*self.nivel*self.vitalidad) )
        self.aplicar_bonuses_de_stats()

class Bardo(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.habilidad_pasiva = clases["bardo"]["habilidad_pasiva"]
        self.vitalidad = clases["bardo"]["atributos"]["vitalidad"]
        self.fuerza = clases["bardo"]["atributos"]["fuerza"]
        self.inteligencia = clases["bardo"]["atributos"]["inteligencia"]
        self.velocidad = clases["bardo"]["atributos"]["velocidad"]
        self.talento = clases["bardo"]["atributos"]["talento"]
        self.observacion = clases["bardo"]["atributos"]["observacion"]
        self.puntos_de_enfoque = clases["bardo"]["atributos"]["puntos_de_enfoque"]
        self.suerte = clases["bardo"]["atributos"]["vitalidad"]
        self.puntos_de_vida = int( self.vida_base + self.nivel + (0.10*self.nivel*self.vitalidad) )
        self.aplicar_bonuses_de_stats()

class Enemigo(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.habilidad_pasiva = clases["bardo"]["habilidad_pasiva"]
        self.vitalidad = clases["bardo"]["atributos"]["vitalidad"]
        self.fuerza = clases["bardo"]["atributos"]["fuerza"]
        self.inteligencia = clases["bardo"]["atributos"]["inteligencia"]
        self.velocidad = clases["bardo"]["atributos"]["velocidad"]
        self.talento = clases["bardo"]["atributos"]["talento"]
        self.observacion = clases["bardo"]["atributos"]["observacion"]
        self.puntos_de_enfoque = clases["bardo"]["atributos"]["puntos_de_enfoque"]
        self.suerte = clases["bardo"]["atributos"]["vitalidad"]
        self.puntos_de_vida = int( self.vida_base + self.nivel + (0.10*self.nivel*self.vitalidad) )
        self.aplicar_bonuses_de_stats()