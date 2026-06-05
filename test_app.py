from app import inventario, agregar_producto, eliminar_producto

def test_agregar():
    inventario.clear()
    agregar_producto("Teclado")
    assert "Teclado" in inventario

def test_eliminar():
    inventario.clear()
    agregar_producto("Monitor")
    eliminar_producto("Monitor")
    assert "Monitor" not in inventario