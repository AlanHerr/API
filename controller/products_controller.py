
"""
Controlador de productos: define los endpoints REST para CRUD de productos.
Todos los endpoints están protegidos con JWT.
"""

from flask import Blueprint, jsonify, request
from service.products_service import (
    list_products,
    get_product,
    add_product,
    modify_product,
    remove_product
)
from flask_jwt_extended import jwt_required

# Crear blueprint para agrupar rutas de productos
products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    """
    Obtener todos los productos (requiere JWT).
    Devuelve una lista de productos en formato JSON.
    """
    products = list_products()
    products_list = [p.__dict__ for p in products]
    for p in products_list:
        p.pop('_sa_instance_state', None)
    return jsonify(products_list), 200

@products_bp.route('/products/<int:product_id>', methods=['GET'])
@jwt_required()
def get_product_route(product_id):
    """
    Obtener un producto por ID (requiere JWT).
    Devuelve el producto si existe, o error 404 si no se encuentra.
    """
    product = get_product(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    prod_dict = product.__dict__
    prod_dict.pop('_sa_instance_state', None)
    return jsonify(prod_dict), 200

@products_bp.route('/products', methods=['POST'])
@jwt_required()
def create_product_route():
    """
    Crear un nuevo producto (requiere JWT).
    Recibe JSON con name, category, price, quantity.
    Devuelve el producto creado o error 400 si faltan datos.
    """
    data = request.json
    if not data or not all(k in data for k in ('name', 'category', 'price', 'quantity')):
        return jsonify({'error': 'Bad request'}), 400
    product = add_product(data)
    prod_dict = product.__dict__
    prod_dict.pop('_sa_instance_state', None)
    return jsonify(prod_dict), 201

@products_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product_route(product_id):
    """
    Actualizar un producto existente (requiere JWT).
    Recibe JSON con los campos a modificar.
    Devuelve el producto actualizado o error 404 si no existe.
    """
    data = request.json
    if not data:
        return jsonify({'error': 'Bad request'}), 400
    product = modify_product(product_id, data)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    prod_dict = product.__dict__
    prod_dict.pop('_sa_instance_state', None)
    return jsonify(prod_dict), 200

@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product_route(product_id):
    """
    Eliminar un producto por ID (requiere JWT).
    Devuelve mensaje de éxito o error 404 si no existe.
    """
    product = remove_product(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'result': 'Product deleted'}), 200