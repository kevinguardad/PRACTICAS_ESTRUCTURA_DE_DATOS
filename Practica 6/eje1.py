# ----------------------------
# Estructura básica: Nodo
# ----------------------------
class Nodo:
    """
    Clase que representa un nodo de un árbol binario.
    Atributos:
    - valor: dato almacenado en el nodo.
    - izq: referencia al hijo izquierdo (otra instancia de Nodo o None).
    - der: referencia al hijo derecho (otra instancia de Nodo o None).
    """
    def __init__(self, valor):
        self.valor = valor    # guardamos el dato
        self.izq = None       # inicialmente no tiene hijo izquierdo
        self.der = None       # inicialmente no tiene hijo derecho

# ----------------------------
# Recorridos recursivos
# ----------------------------
def preorden(nodo):
    """
    Preorden: visitar raíz -> izquierda -> derecha
    Usamos recursión: si el nodo es None (vacío) no hacemos nada.
    """
    if nodo:                        # caso base implícito: si nodo es None, no entramos
        print(nodo.valor, end=" ")  # 1) Visito la raíz (proceso: imprimir el valor)
        preorden(nodo.izq)         # 2) Recorro recursivamente el subárbol izquierdo
        preorden(nodo.der)         # 3) Recorro recursivamente el subárbol derecho

def inorden(nodo):
    """
    Inorden: izquierda -> raíz -> derecha
    Útil en BST (imprime valores ordenados).
    """
    if nodo:
        inorden(nodo.izq)          # 1) Primero todo el lado izquierdo
        print(nodo.valor, end=" ") # 2) Luego la raíz
        inorden(nodo.der)          # 3) Luego todo el lado derecho

def postorden(nodo):
    """
    Postorden: izquierda -> derecha -> raíz
    Útil para liberar memoria o eliminar nodos (visitar hijos antes que la raíz).
    """
    if nodo:
        postorden(nodo.izq)        # 1) Izquierda
        postorden(nodo.der)        # 2) Derecha
        print(nodo.valor, end=" ") # 3) Raíz (al final)
        
# ----------------------------
# Recorrido por niveles (BFS)
# ----------------------------
from collections import deque

def bfs(raiz):
    """
    Breadth-First Search (recorrido por niveles).
    Emplea una cola (FIFO). 
    Pasos: encolar la raíz; mientras la cola no esté vacía:
           desapilar (popleft), procesar, encolar sus hijos (izq, der).
    """
    if not raiz:
        return
    q = deque([raiz])              # inicializamos la cola con la raíz
    while q:
        nodo = q.popleft()         # sacamos el primer elemento (FIFO)
        print(nodo.valor, end=" ")
        if nodo.izq:               # si tiene hijo izquierdo, lo encolamos
            q.append(nodo.izq)
        if nodo.der:               # si tiene hijo derecho, lo encolamos
            q.append(nodo.der)

# ----------------------------
# Árbol Binario de Búsqueda (BST): Insertar y Buscar (iterativo)
# ----------------------------
class NodoBST:
    """
    Nodo específico para BST (mismo concepto que Nodo pero separado por claridad).
    """
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def insertar_bst(root, valor):
    """
    Insertar un valor en un BST (recursivo).
    - Si root es None: creamos nuevo nodo y lo devolvemos.
    - Si valor < root.valor: lo insertamos en el subárbol izquierdo.
    - Si valor > root.valor: lo insertamos en el subárbol derecho.
    (No insertamos duplicados en este ejemplo.)
    """
    if root is None:
        return NodoBST(valor)      # caso base: sitio encontrado para insertar
    if valor < root.valor:
        root.izq = insertar_bst(root.izq, valor)  # descendemos izquierda
    elif valor > root.valor:
        root.der = insertar_bst(root.der, valor)  # descendemos derecha
    return root                    # retornamos la raíz (sin cambios si ya existía)

def buscar_bst(root, valor):
    """
    Búsqueda iterativa en BST para mostrar el camino seguido.
    Retorna el nodo si lo encuentra, o None si no.
    También imprime el camino (secuencia de valores comparados).
    """
    camino = []
    nodo = root
    while nodo:
        camino.append(nodo.valor)   # registramos el nodo que vamos visitando
        if valor == nodo.valor:
            print("Camino de búsqueda:", " -> ".join(map(str, camino)))
            return nodo            # encontrado
        elif valor < nodo.valor:
            nodo = nodo.izq        # vamos al subárbol izquierdo
        else:
            nodo = nodo.der        # vamos al subárbol derecho
    print("Camino de búsqueda:", " -> ".join(map(str, camino)))
    return None                   # no encontrado

# ----------------------------
# Altura y conteo de nodos (recursivo)
# ----------------------------
def altura(nodo):
    """
    Altura medida en número de nodos en el camino más largo desde este nodo hasta una hoja.
    - Si nodo es None: altura 0.
    - Sino: 1 + max(altura(izq), altura(der))
    Nota: si prefieres aristas (edges), devuelve altura(nodo)-1.
    """
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izq), altura(nodo.der))

def contar_nodos(nodo):
    """
    Cuenta recursivamente todos los nodos del árbol.
    - Si nodo es None: 0
    - Sino: 1 + contar(izq) + contar(der)
    """
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.izq) + contar_nodos(nodo.der)

# ----------------------------
# Invertir (mirror) el árbol
# ----------------------------
def invertir(nodo):
    """
    Convierte el árbol en su espejo intercambiando los hijos izquierdo y derecho en cada nodo.
    Realiza el swap en el nodo actual y luego llama recursivamente a los hijos.
    """
    if nodo is None:
        return
    # swap de hijos
    nodo.izq, nodo.der = nodo.der, nodo.izq
    # aplicar recursión en los nuevos hijos
    invertir(nodo.izq)
    invertir(nodo.der)

# ----------------------------
# Construcción del árbol de ejemplo (usado en ejercicios 1,2,4,5)
# ----------------------------
def construir_arbol_ejemplo():

#    Construye un árbol con la forma:
#           1
#         /   \
#        2     3
#       / \   / \
#      4   5 6   7
#         /
#        8
#    y devuelve la raíz.

    raiz = Nodo(1)
    raiz.izq = Nodo(2); raiz.der = Nodo(3)
    raiz.izq.izq = Nodo(4); raiz.izq.der = Nodo(5)
    raiz.der.izq = Nodo(6); raiz.der.der = Nodo(7)
    raiz.izq.der.izq = Nodo(8)
    return raiz

# ----------------------------
# Bloque principal: ejecutar ejercicios y mostrar salidas
# ----------------------------
if __name__ == "__main__":
    print("=== EJERCICIO 1: Preorden / Inorden / Postorden ===")
    raiz = construir_arbol_ejemplo()
    print("Preorden: ", end=""); preorden(raiz); print()
    print("Inorden:  ", end=""); inorden(raiz); print()
    print("Postorden:", end=""); postorden(raiz); print()
    print()

    print("=== EJERCICIO 2: Recorrido por niveles (BFS) ===")
    print("BFS: ", end=""); bfs(raiz); print()
    print()

    print("=== EJERCICIO 3: BST insertar y buscar ===")
    valores = [50,30,20,40,70,60,80]
    root_bst = None
    for v in valores:
        root_bst = insertar_bst(root_bst, v)   # insertamos en el BST
    # mostramos camino de búsqueda para 60 (debería encontrarlo)
    res = buscar_bst(root_bst, 60)
    print("Resultado búsqueda 60:", res.valor if res else "No encontrado")
    # y un ejemplo no encontrado (25)
    res2 = buscar_bst(root_bst, 25)
    print("Resultado búsqueda 25:", res2.valor if res2 else "No encontrado")
    print()

    print("=== EJERCICIO 4: Altura y conteo de nodos ===")
    print("Altura (en nodos):", altura(raiz))
    print("Número total de nodos:", contar_nodos(raiz))
    print()

    print("=== EJERCICIO 5: Invertir (mirror) el árbol ===")
    print("Preorden original: ", end=""); preorden(raiz); print()
    invertir(raiz)
    print("Preorden invertido:", end=" "); preorden(raiz); print()
    # restaurar (invertir otra vez)
    invertir(raiz)
    print("Preorden restaurado:", end=" "); preorden(raiz); print()