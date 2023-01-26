import pygame
from Base_de_Datos import *
from Azar import *
from Sprites import SpriteParaAventurero


class HabitanteDeFahrul:

    tamano_sprite_pequeno = (55,55)
    def __init__(self):
        self.arma = None
        self.nivel = 0
        self.dano_de_ataque = None
        self.armadura = 0
        self.resistencia = 0
        self.evasion = None
        self.velocidad = None
        self.puntos_de_vida = None
        self.vida_actual = None
    
    def __repr__(self) -> str:
        return str(self.nombre)


class Criatura(HabitanteDeFahrul):
    def __init__(self, nombre, nivel=0):
        super().__init__()
        datosCriatura = Criatura.obtener_datos_de_criatura(nombre)
        self.nivel = nivel
        self.nombre = datosCriatura[1]        
        self.velocidad = datosCriatura[2]
        self.puntos_de_vida = datosCriatura[4] + nivel*3
        self.puntos_de_ataque = datosCriatura[5]
        self.armadura = datosCriatura[6]
        self.resistencia = datosCriatura[7]
        self.evasion = datosCriatura[8]
        self.vida_actual = self.puntos_de_vida
        self.sprite = pygame.transform.scale(pygame.image.load(datosCriatura[9]), HabitanteDeFahrul.tamano_sprite_pequeno)
    

    @staticmethod
    def obtener_datos_de_criatura(nombreDeCriatura):
        conn = sql.connect("For_The_Queen.db")
        cursor = conn.cursor()
        instruccion = f"SELECT * FROM criaturas WHERE nombre='{nombreDeCriatura}'"
        cursor.execute(instruccion)
        datos = cursor.fetchall()[0]
        conn.commit()
        return datos
    
    def atacar(self):
        pass


class Aventurero(HabitanteDeFahrul):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.inventario = []
        self.arma = None
        self.escudo = None
        self.casco = None
        self.collar = None
        self.armadura_torso = None
        self.botas = None

        self.vitalidad = None
        self.fuerza = None
        self.inteligencia = None
        self.velocidad = None
        self.talento = None
        self.observacion = None
        self.suerte = None

        self.vida_base = 15
        self.puntos_de_enfoque = None
        self.puntos_de_movimiento_maximo = 5
        self.experiencia = 0

        self.nivel = 1
        self.casilla_inicial = None
        self.casilla_ocupada = None
        self.imagen = None
        self.rect = None
        
        #comunicar posicion del personaje al tablero y a la interfaz
        

    
    @staticmethod
    def obtener_datos_de_clase(clase_del_aventurero):
        conn = sql.connect("For_The_Queen.db")
        cursor = conn.cursor()
        instruccion = f"SELECT * FROM clases WHERE nombre='{clase_del_aventurero}'"
        cursor.execute(instruccion)
        datos = cursor.fetchall()[0]
        conn.commit()
        return datos
    
    
    def agregar_informacion_de_clase(self, clase):
        datosDeClase = Aventurero.obtener_datos_de_clase(clase)
        self.arma = datosDeClase[2]
        self.habildiad_pasiva = datosDeClase[3]
        self.vitalidad = datosDeClase[4]
        self.fuerza = datosDeClase[5]
        self.inteligencia = datosDeClase[6]
        self.velocidad = datosDeClase[7]
        self.talento = datosDeClase[8]
        self.observacion = datosDeClase[9]
        self.suerte = datosDeClase[10]
        self.armadura = datosDeClase[11]
        self.resistencia = datosDeClase[12]
        self.evasion = datosDeClase[13]
        self.puntos_de_enfoque = datosDeClase[14]
        self.puntos_de_vida = int( self.vida_base + self.nivel + (0.10*self.nivel*self.vitalidad) )
        self.imagen = pygame.transform.scale(pygame.image.load(datosDeClase[15]), HabitanteDeFahrul.tamano_sprite_pequeno)
        self.sprite = SpriteParaAventurero(self.imagen)
        self.rect = self.imagen.get_rect()


    def aplicar_bonuses_de_stats(self):
        if self.fuerza > 50:
            self.armadura += 1
        if self.inteligencia > 50:
            self.resistencia += 1
    

    def subir_de_nivel(self):
        self.nivel += 1
        self.dano_de_ataque += 1
        if type(self) == Herrero:
            self.puntos_de_vida += 11
        elif type(self) == Erudito:
            self.puntos_de_vida += 8
        elif type(self) == Cazador:
            self.puntos_de_vida += 9
        elif type(self) == Bardo:
            self.puntos_de_vida += 8
    
    
    def ganar_experiencia(self, exp):
        self.experiencia += exp
        if self.puede_levelear():
            self.subir_de_nivel()


    def puede_levelear(self): 
        niveles = {
        0:	0,
        1:	25,
        2:	70,
        3:	130,
        4:	220,
        5:	350,
        6:	510,
        7:	720,
        8:	1100,
        9:	1600,
        10:	2200,
        11:	3200,
        12:	4600,
        13:	6800,
        14:	10000
        }
        if self.experiencia > niveles[self.nivel]:#si tengo mas exp que el max correspondiente a ese nivel, lvleo
            return True
            

    def atacar(self, objetivo):
        pass


    def calcular_dano_causado(self, objetivo):
        habilidad = self.arma.habilidad
        dano = self.dano_de_ataque + self.arma.dano_base
        afinidad = self.arma.afinidad
        chances_de_exito = self.afinidad
        rolls = Azar.rollear_dados(chances_de_exito, self.arma.cantidad_de_rolls)


    def calcular_dano_recibido(self, atacante):
        pass


    def get_posicion(self):
        pass
    

    
        
        
class Herrero(Aventurero):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.clase = "herrero"
        self.nombre = nombre
        self.agregar_informacion_de_clase(self.clase)
        self.aplicar_bonuses_de_stats()
        self.vida_actual = self.puntos_de_vida


        

class Erudito(Aventurero):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.clase = "erudito"
        self.nombre = nombre
        self.agregar_informacion_de_clase(self.clase)
        self.aplicar_bonuses_de_stats()
        self.vida_actual = self.puntos_de_vida



class Cazador(Aventurero):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.clase = "cazador"
        self.nombre = nombre
        self.agregar_informacion_de_clase(self.clase)
        self.aplicar_bonuses_de_stats()
        self.vida_actual = self.puntos_de_vida


class Bardo(Aventurero):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.clase = "bardo"
        self.nombre = nombre
        self.agregar_informacion_de_clase(self.clase)
        self.aplicar_bonuses_de_stats()
        self.vida_actual = self.puntos_de_vida


'''
erudito = Erudito("juan_sabio")
criatura = Criatura("lobo")

print(erudito.puntos_de_vida)
print(criatura.puntos_de_vida)
'''