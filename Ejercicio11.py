# Crear tuplas de estudiantes: (nombre, apellido, edad, carrera, promedio)
est1 = ("Ana", "Martínez", 19, "Ingeniería de Software", 8.7)
est2 = ("Luis", "Jiménez", 21, "Ingeniería en Sistemas", 9.2)
est3 = ("Camila", "Flores", 20, "Ingeniería de Datos", 8.9)
est4 = ("José", "Ramos", 22, "Ingeniería en Redes", 7.8)

# Lista con todos los estudiantes
estudiantes = [est1, est2, est3, est4]

print("=== Registro de Estudiantes ===")
for est in estudiantes:
    # Unpacking de la tupla
    nombre, apellido, edad, carrera, promedio = est
    print(f"Nombre: {nombre} {apellido} | Edad: {edad} | Carrera: {carrera} | Promedio: {promedio}")

# Encontrar el estudiante con mejor promedio
mejor_est = max(estudiantes, key=lambda e: e[4])  # índice 4 = promedio
print(f"\nEl estudiante con mejor promedio es {mejor_est[0]} {mejor_est[1]} con {mejor_est[4]}")