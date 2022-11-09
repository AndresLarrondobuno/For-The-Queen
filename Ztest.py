class Persona:
    cantidad_de_ojos = 2
    cantidad_de_piernas = 2 #en el mejor de los casos

    def __init__(self, nombre, edad, altura, peso, coeficiente_intelectual):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso= peso
        self.coeficiente_intelectual = coeficiente_intelectual
    
    def existir(self):
        print("existo")

pepe = Persona('pepe', 20, 1.8, 78, 185)
juan = Persona('juan', 38, 1.75, 80, 180)

pepe.existir()



        
