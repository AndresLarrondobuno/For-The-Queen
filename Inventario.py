from Item import *

class Inventario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.items = list()
    
    def agregar_item(self, item):
        self.items.append(item)
    
    def agrupar_items(self):
        items_agrupados = dict()
        for item in self.items:
            if item.nombre not in items_agrupados:
                items_agrupados[item.nombre] = 1
            else:
                items_agrupados[item.nombre] += 1
        return 
    
    def __repr__(self) -> str:
        return f"{self.nombre}: {self.items}"




