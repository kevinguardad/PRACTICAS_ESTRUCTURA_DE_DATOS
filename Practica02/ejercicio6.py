#Ejercicio6: Trabajar con listas de materias de ingenieria de software

#a) Crear lista con 5 materias
materias = ["Programacion", "Estructura de datos", "Base de Datos", "Ingenieria de Software", "Redes"]

#Mostrar la lista completa
print("Lista inicial de materias: ", materias)

# b) Agregar 2 materias mas usando append()
materias.append("Sistemas operativos")
materias.append("Inteligencia Artificial")
print("Lista despues de agregar 2 materias: ", materias)

# c) Insertar una materia en la posicion 2
materias.insert(2, "Materias Discretas")
print("Lista despues de insertar una materia en la posicion 2: ", materias)

#d) Eliminar la ultima materia usando remove()
ultima_materia = materias[-1]
materias.remove(ultima_materia)
print("Lista despues de eliminar la ultima materia: ", materias)

# e) Mostrar el numero total de materias
print("Numero total de materias: ", len(materias))
