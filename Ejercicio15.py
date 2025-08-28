# Ejercicio 15: Materias de diferentes carreras

# Crear 3 conjuntos de materias
software = {"Programación", "Base de Datos", "Redes", "Ingeniería de Software", "Matemáticas Discretas", "Sistemas Operativos"}
sistemas = {"Programación", "Estructura de Datos", "Redes", "Arquitectura de Computadoras", "Sistemas Operativos", "Matemáticas"}
datos = {"Programación", "Estadística", "Base de Datos", "Minería de Datos", "Inteligencia Artificial", "Matemáticas"}

# Materias comunes entre todas las carreras
comunes = software & sistemas & datos
print("Materias comunes en todas las carreras:", comunes)

# Materias exclusivas de cada carrera
print("Exclusivas de Software:", software - (sistemas | datos))
print("Exclusivas de Sistemas:", sistemas - (software | datos))
print("Exclusivas de Datos:", datos - (software | sistemas))

# Unión de todas las materias
union_materias = software | sistemas | datos
print("\nUnión de todas las materias:", union_materias)

# Número total de materias únicas
print("Total de materias únicas:", len(union_materias))