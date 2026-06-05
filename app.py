from flask import Flask, jsonify, request

app = Flask(__name__)

inventario = []

@app.route("/")
def home():
    return "API de Inventario funcionando 🚀"

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(inventario)

@app.route("/productos", methods=["POST"])
def agregar_producto():
    data = request.get_json()
    inventario.append(data["nombre"])
    return jsonify({"mensaje": "Producto agregado", "inventario": inventario})

@app.route("/productos/<nombre>", methods=["DELETE"])
def eliminar_producto(nombre):
    if nombre in inventario:
        inventario.remove(nombre)
        return jsonify({"mensaje": "Eliminado", "inventario": inventario})
    return jsonify({"error": "No encontrado"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)