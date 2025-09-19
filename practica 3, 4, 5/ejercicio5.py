class Cola:
    def __init__(self):
        self.elementos = []
    def esta_vacia(self):
        return len(self.elementos) == 0
    def encolar(self, item):
        self.elementos.append(item)
    def desencolar(self):
        return self.elementos.pop(0) if not self.esta_vacia() else "Cola vacía"
    
cola_comidas = Cola()
cola_comidas.encolar("Oden de tacos") 
cola_comidas.encolar("Orden de pizza")
cola_comidas.encolar("Oden de hamburguesa")

print("Entrega primero: ", cola_comidas.desencolar())
print("Quedan en la fila: ", cola_comidas.elementos)