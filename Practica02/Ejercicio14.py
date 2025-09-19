# Ejercicio 14: Agenda de contactos

# Diccionario vacío
contactos = {}

# Funciones
def agregar_contacto(nombre, telefono, email):
    contactos[nombre] = {"telefono": telefono, "email": email}
    print(f"Contacto '{nombre}' agregado correctamente.")

def buscar_contacto(nombre):
    if nombre in contactos:
        print(f"Nombre: {nombre}, Teléfono: {contactos[nombre]['telefono']}, Email: {contactos[nombre]['email']}")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

def mostrar_contactos():
    if contactos:
        print("\n=== Lista de contactos ===")
        for nombre, info in contactos.items():
            print(f"- {nombre}: Teléfono: {info['telefono']}, Email: {info['email']}")
    else:
        print("No hay contactos registrados.")

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado correctamente.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

def actualizar_contacto(nombre, telefono=None, email=None):
    if nombre in contactos:
        if telefono:
            contactos[nombre]["telefono"] = telefono
        if email:
            contactos[nombre]["email"] = email
        print(f"Contacto '{nombre}' actualizado correctamente.")
    else:
        print(f"Contacto '{nombre}' no encontrado.")

# Agregar 5 contactos iniciales
agregar_contacto("Ana", "1234-5678", "ana@email.com")
agregar_contacto("Luis", "9876-5432", "luis@email.com")
agregar_contacto("Camila", "4567-8901", "camila@email.com")
agregar_contacto("José", "7654-3210", "jose@email.com")
agregar_contacto("Marta", "1111-2222", "marta@email.com")

# Probar funciones
print()
mostrar_contactos()
print()
buscar_contacto("Luis")
print()
actualizar_contacto("Ana", telefono="0000-1111")
eliminar_contacto("Marta")
print()
mostrar_contactos()