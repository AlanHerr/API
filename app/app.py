from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Datos simulados: productos de una tienda
inventory = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 1200,
        "quantity": 50
    },
    {
        "id": 2,
        "name": "Smartphone",
        "category": "Electronics",
        "price": 800,
        "quantity": 100
    },
    {
        "id": 3,
        "name": "T-shirt",
        "category": "Clothing",
        "price": 25,
        "quantity": 200
    }
]

# Obtener todos los productos
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(inventory), 200

# Obtener un producto por ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in inventory if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product), 200

# Crear un nuevo producto
@app.route('/products', methods=['POST'])
def create_product():
    if not request.json or 'name' not in request.json or 'category' not in request.json or 'price' not in request.json or 'quantity' not in request.json:
        return jsonify({'error': 'Bad request'}), 400
    new_id = max(p['id'] for p in inventory) + 1 if inventory else 1
    product = {
        'id': new_id,
        'name': request.json['name'],
        'category': request.json['category'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    inventory.append(product)
    return jsonify(product), 201

# Actualizar un producto existente
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in inventory if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    if not request.json:
        return jsonify({'error': 'Bad request'}), 400
    product['name'] = request.json.get('name', product['name'])
    product['category'] = request.json.get('category', product['category'])
    product['price'] = request.json.get('price', product['price'])
    product['quantity'] = request.json.get('quantity', product['quantity'])
    return jsonify(product), 200

# Eliminar un producto
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((p for p in inventory if p['id'] == product_id), None)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    inventory.remove(product)
    return jsonify({'result': 'Product deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
