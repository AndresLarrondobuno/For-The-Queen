import random as rng
class Azar:

    def rollear_dados(porcentaje_de_exito, cantidad_de_rolls, cantidad_de_rolls_asegurados=0): #devuelve True si el dado cae dentro del rango indicado por el %
        resultados_de_rolls = [True for x in range(cantidad_de_rolls_asegurados)] 
        chances_de_exito_por_roll = ( (porcentaje_de_exito/100)**(1/cantidad_de_rolls) )*100
        cantidad_de_rolls_no_asegurados = cantidad_de_rolls - cantidad_de_rolls_asegurados
        for roll_no_asegurado in range(cantidad_de_rolls_no_asegurados):
            resultados_de_rolls.append(Azar.roll(chances_de_exito_por_roll))
        return resultados_de_rolls
    

    def roll(porcentaje_de_exito):
        return (rng.randint(1,100) <= porcentaje_de_exito)
    

    def asegurar_rolls(cantidad_de_rolls_asegurados):
        pass


    def casilla_al_azar(casillas):
        casilla_inicial = rng.choice(list(casillas))
        return casilla_inicial
    

    def roll_de_movimiento(personaje):
        movimientos_disponibles = personaje.puntos_de_movimiento_maximo
        resultado = rng.choice(range(movimientos_disponibles))
        return resultado













    






