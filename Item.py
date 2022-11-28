from Base_de_Datos import *

class Item:
    def __init__(self, nombre):
        self.datosDeItem = Item.obtener_datos_de_item(nombre)
        
    
    @staticmethod
    def obtener_datos_de_item(nombre_de_item):
        tipo_de_item = Item.clasificar_item_por_tipo(nombre_de_item)
        conn = sql.connect("For_The_Queen.db")
        cursor = conn.cursor()
        instruccion = f"SELECT * FROM {tipo_de_item} WHERE nombre='{nombre_de_item}'"
        cursor.execute(instruccion)
        datos = cursor.fetchall()[0]
        conn.commit()
        return datos


    @staticmethod
    def clasificar_item_por_tipo(nombre_de_item):
        if nombre_de_item in armas.keys():
            return "armas"
        elif nombre_de_item in armaduras.keys():
            return "armaduras"
        elif nombre_de_item in consumibles.keys():
            return "consumibles"

    def __repr__(self) -> str:
        return self.nombre
        

class Item_Equipable(Item):
    def __init__(self, nombre):
        super().__init__(nombre)


class Item_Consumible(Item):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = self.datosDeItem[1]
        self.dano_base = self.datosDeItem[2]
        self.curacion_base = self.datosDeItem[3]
        self.efecto_en_tablero = self.datosDeItem[4]
        self.efecto_en_combate = self.datosDeItem[5]


class Item_Miscelaneo(Item):
    def __init__(self):
        super().__init__()


class Arma(Item_Equipable):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = self.datosDeItem[1]
        self.habilidades = (self.datosDeItem[2]).split(" ")
        self.calidad = self.datosDeItem[3]
        self.dano_base = self.datosDeItem[4]
        self.tipo_de_dano = self.datosDeItem[5]
        self.afinidad = self.datosDeItem[6]
        self.bonus_vitalidad = self.datosDeItem[7]
        self.bonus_fuerza = self.datosDeItem[8]
        self.bonus_inteligencia = self.datosDeItem[9]
        self.bonus_velocidad = self.datosDeItem[10]
        self.bonus_talento = self.datosDeItem[11]
        self.bonus_observacion = self.datosDeItem[12]
        self.bonus_suerte = self.datosDeItem[13]
        self.bonus_armadura = self.datosDeItem[14]
        self.bonus_resistencia = self.datosDeItem[15]
        self.evasion = self.datosDeItem[16]
        self.enfoque = self.datosDeItem[17]


class Armadura(Item_Equipable):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nombre = self.datosDeItem[1]
        self.habilidad_pasiva = self.datosDeItem[2]
        self.calidad = self.datosDeItem[3]
        self.bonus_vitalidad = self.datosDeItem[4]
        self.bonus_fuerza = self.datosDeItem[5]
        self.bonus_inteligencia = self.datosDeItem[6]
        self.bonus_velocidad = self.datosDeItem[7]
        self.bonus_talento = self.datosDeItem[8]
        self.bonus_observacion = self.datosDeItem[9]
        self.bonus_suerte = self.datosDeItem[10]
        self.bonus_armadura = self.datosDeItem[11]
        self.bonus_resistencia = self.datosDeItem[12]
        self.evasion = self.datosDeItem[13]
        self.enfoque = self.datosDeItem[14]
