from Item import *
from HabitanteDeFahrul import *
from Casilla import *
from Tablero import *


class EventoDeFahrul:
    def __init__(self, casilla_trigger):
        self.casilla_trigger = casilla_trigger
        self.activado = False


class Tienda(EventoDeFahrul):
    def __init__(self, casilla_trigger):
        super().__init__(casilla_trigger)
        self.inventario = None
        self.sprite = pygame.transform.scale(pygame.image.load(r"C:\Users\54115\Desktop\python\For The Queen\assets\dc-dngn\shops\dngn_enter_shop.png"),(36,36))
        self.visible = True


class Desafio(EventoDeFahrul):
    def __init__(self, casilla_trigger):
        super().__init__(casilla_trigger)
        self.visible = False


class Enfrentamiento(EventoDeFahrul):
    def __init__(self, casilla_trigger):
        super().__init__(casilla_trigger)
        self.visible = True


class Emboscada(Enfrentamiento):
    def __init__(self, casilla_trigger):
        super().__init__(casilla_trigger)
        self.visible == False


