from flask import Flask, jsonify, request

app = Flask(__name__)

inventario = []

# 🔧 lógica reutilizable
def agregar_producto(nombre):
    inventario.append(nombre)
    return nombre

def eliminar_producto(nombre):
    if nombre in inventario:
        inventario.remove(nombre)
        return True
    return False


# 🌐 API Flask
@app.route("/")
def home():
    return "API de Inventario funcionando 🚀"

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(inventario)

@app.route("/productos", methods=["POST"])
def agregar_producto_route():
    data = request.get_json()
    agregar_producto(data["nombre"])
    return jsonify({"mensaje": "Producto agregado", "inventario": inventario})

@app.route("/productos/<nombre>", methods=["DELETE"])
def eliminar_producto_route(nombre):
    if eliminar_producto(nombre):
        return jsonify({"mensaje": "Eliminado", "inventario": inventario})
    return jsonify({"error": "No encontrado"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)