class Habilidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.efecto = None
        self.dano_en_area =  False
        self.multiplicador_de_dano = None
        self.rolls = None