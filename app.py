inventario = []

def agregar_producto(nombre):
    inventario.append(nombre)
    return f"Producto '{nombre}' agregado."

def eliminar_producto(nombre):
    if nombre in inventario:
        inventario.remove(nombre)
        return f"Producto '{nombre}' eliminado."
    return "Producto no encontrado."

if __name__ == "__main__":
    print("=== Sistema de Inventario ===")

    agregar_producto("Laptop")
    agregar_producto("Mouse")

    print("Inventario actual:")
    print(inventario)

    eliminar_producto("Mouse")

    print("Inventario después de eliminar:")
    print(inventario)