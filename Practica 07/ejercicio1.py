class NodoCategoria :
    def __init__(self, id_categoria, nombre):     
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.izquierdo = None
        self.derecho = None

#Insertar categorias
def insertar(raiz, id_categoria, nombre):
    if raiz is None:
        return NodoCategoria(id_categoria, nombre)
    elif id_categoria < raiz.id_categoria:
        raiz.izquierdo = insertar(raiz.izquierdo, id_categoria, nombre)
    else:
        raiz.derecho = insertar(raiz.derecho, id_categoria, nombre)
    return raiz

#Buscar categoria
def buscar(raiz, id_categoria):
    if raiz is None or raiz.id_categoria == id_categoria:
        return raiz
    if id_categoria < raiz.id_categoria:
        return buscar(raiz.izquierdo, id_categoria)
    return buscar(raiz.derecho, id_categoria)

#Recorrido Inorden 
def recorrido_inorden(raiz):
    if raiz:
        recorrido_inorden(raiz.izquierdo)
        print(f"ID: {raiz.id_categoria}, Nombre: {raiz.nombre}")
        recorrido_inorden(raiz.derecho)

 #Ejemplo de uso
raiz = None
categorias= [

    (50, "Biblioteca"),
    (30, "Literatura"),
    (20, "Novela"),
    (40, "Poesia"),
    (70, "Ciencia"),
    (60, "Matematicas"),
    (80, "Historia")
]

for id_categoria, nombre in categorias:
    raiz = insertar(raiz, id_categoria, nombre)

print("Recorrido Inorden de las categorias:")
recorrido_inorden(raiz)

print("\nBuscando categoria con ID 60:")
resultado = buscar(raiz, 60)
if resultado:
    print(f"Encontrada: {resultado.nombre}")

else:
    print("Categoria no encontrada")