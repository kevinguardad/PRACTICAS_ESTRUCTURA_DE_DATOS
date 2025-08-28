import math 
#Crear 5 tuplas que representan coordenadas (x, y)
p1 = (2, 3)
p2 = (5, 1)
p3 = (-3, -4)
p4 = (0, 7)
p5 = (6, -2)

#Almacenar las tuplasen una lista 
puntos = [p1, p2, p3, p4, p5]

#Calcular la distancia de cada punto al origen (0,0)
distancias = []
for punto in puntos:
    x, y = punto
    distancia = math.sqrt(x**2 + y**2)
    distancias.append(distancia)
    print(f"Punto {punto}= Distancia al origen: {distancia:.2f}")

#Encontrar el punto mas cercano al origen
min_dist = min(distancias)
indice = distancias.index(min_dist)
print(f"\nEl punto mas cercano al origen es {puntos[indice]} con distancia {min_dist:.2f}") 
