# Ejercicio 16: Sistema de permisos con conjuntos

# Conjuntos de permisos
admin = {"crear", "leer", "actualizar", "eliminar", "administrar"}
profesor = {"crear", "leer", "actualizar", "calificar"}
estudiante = {"leer", "participar"}

# Verificar si un usuario tiene un permiso específico
permiso = "eliminar"
print(f"¿El admin tiene permiso '{permiso}'? ->", permiso in admin)
print(f"¿El profesor tiene permiso '{permiso}'? ->", permiso in profesor)
print(f"¿El estudiante tiene permiso '{permiso}'? ->", permiso in estudiante)

# Permisos únicos de cada rol
print("\nPermisos únicos de admin:", admin - (profesor | estudiante))
print("Permisos únicos de profesor:", profesor - (admin | estudiante))
print("Permisos únicos de estudiante:", estudiante - (admin | profesor))

# Crear super_admin con todos los permisos
super_admin = admin | profesor | estudiante
print("\nPermisos de super_admin:", super_admin)