class Cola:
    def __init__(self):
        self.elementos = []
    def esta_vacia(self):
        return len(self.elementos) == 0
    def encolar(self, item):
        self.elementos.append(item)
    def desencolar(self):
        return self.elementos.pop(0) if not self.esta_vacia() else "Cola vacía"
    
cola_red = Cola()
cola_red.encolar("Archivo1.zip")
cola_red.encolar("Archivo2.mp4")
cola_red.encolar("Archivo3.pdf")

print("Se transmite: ", cola_red.desencolar())
print("En cola de transmisión: ", cola_red.elementos)