# Ejercicio 13: Sistema de inventario

# Diccionario de productos
inventario = {
    "laptop": {"precio": 800, "cantidad": 5, "categoria": "tecnologia"},
    "mouse": {"precio": 25, "cantidad": 20, "categoria": "tecnologia"},
    "silla": {"precio": 60, "cantidad": 10, "categoria": "muebles"},
    "libro": {"precio": 15, "cantidad": 30, "categoria": "papeleria"},
    "impresora": {"precio": 200, "cantidad": 3, "categoria": "tecnologia"}
}

# Calcular el valor total del inventario
valor_total = sum(info["precio"] * info["cantidad"] for info in inventario.values())
print(f"Valor total del inventario: ${valor_total}")

# Mostrar todos los productos de una categoría específica (ejemplo: tecnologia)
categoria = "tecnologia"
print(f"\nProductos en la categoría '{categoria}':")
for producto, info in inventario.items():
    if info["categoria"] == categoria:
        print(f"- {producto} (Precio: {info['precio']}, Cantidad: {info['cantidad']})")

# Actualizar la cantidad de un producto (ejemplo: mouse)
inventario["mouse"]["cantidad"] += 5
print(f"\nCantidad actualizada de mouse: {inventario['mouse']['cantidad']}")