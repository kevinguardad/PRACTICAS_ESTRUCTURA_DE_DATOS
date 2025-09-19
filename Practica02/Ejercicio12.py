# Ejercicio 12: Diccionario de estudiante universitario

# Crear diccionario con la información del estudiante
estudiante = {
    "nombre": "Ana",
    "apellido": "Martínez",
    "edad": 19,
    "carrera": "Ingeniería de Software",
    "materias_cursando": ["Programación", "Base de Datos", "Redes"],
    "promedio": 8.5
}

# Agregar 2 materias más a la lista de materias
estudiante["materias_cursando"].append("Ingeniería de Software")
estudiante["materias_cursando"].append("Matemáticas Discretas")

# Modificar el promedio
estudiante["promedio"] = 9.0

# Agregar nueva clave "semestre"
estudiante["semestre"] = 3

# Mostrar todas las claves y valores del diccionario
print("=== Información del Estudiante ===")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")