class Cola:
    def __init__(self):
        self.elementos = []
    def esta_vacia(self):
        return len(self.elementos) == 0
    def encolar(self, item):
        self.elementos.append(item)
    def desencolar(self):
        return self.elementos.pop(0) if not self.esta_vacia() else "Cola vacía"
    
cola_estudiantes = Cola()
cola_estudiantes.encolar("Sofía")
cola_estudiantes.encolar("Mario")
cola_estudiantes.encolar("Lucía")

print("Entrega primero: ", cola_estudiantes.desencolar())
print("Quedan en la fila: ", cola_estudiantes.elementos)