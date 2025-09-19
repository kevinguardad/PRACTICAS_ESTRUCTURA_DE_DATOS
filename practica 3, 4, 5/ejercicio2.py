class Cola:
    def __init__(self):
        self.elementos = []
    def esta_vacia(self):
        return len(self.elementos) == 0
    def encolar(self, item):
        self.elementos.append(item)
    def desencolar(self):
        return self.elementos.pop(0) if not self.esta_vacia() else "Cola vacía"
    
cola_hospital = Cola()
cola_hospital.encolar("Paciente Juan")
cola_hospital.encolar("Paciente Marta")
cola_hospital.encolar("Paciente Pablo")

print("Atendido: ", cola_hospital.desencolar())
print("En espera: ", cola_hospital.elementos)