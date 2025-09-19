import random

random.seed(42)

#Generamos clientes con tuplas
clientes = [
    ("Cliente1", random.randint(1, 10)),
    ("Cliente2", random.randint(1, 10)),
    ("Cliente3", random.randint(1, 10)),
    ("Cliente4", random.randint(1, 10)),
    ("Cliente5", random.randint(1, 10)),
]

tiempo_acumulado = 0 #tiempo que el cajero ha trabajado
tiempo_espera = [] #lista para guardar tiempos de espera de cada cliente
tiempo_servicio = [] #guarda los tiempos de servicio del cajero

for nombre, servicio in clientes:
    #tiempo de espera del cliente actual
    espera = tiempo_acumulado
    tiempo_espera.append(espera)
    tiempo_servicio.append(servicio)

    print(f"{nombre}: tiempo de servicio{servicio} min, tiempos de espera {espera} min")

    #actualizacion acumulada: despues de atender al cliente en el cajero
    tiempo_acumulado += servicio

#calculos finales
promedio_espera = sum(tiempo_espera) / len(tiempo_espera)
promedio_servicio = sum(tiempo_servicio) / len(tiempo_servicio)

print(f"\nPromedio de espera: {promedio_espera:.2f} min")
print(f"Promedio de servicio: {promedio_servicio:.2f} min")