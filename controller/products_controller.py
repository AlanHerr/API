from flask import Blueprint, jsonify, request
from service.products_service import (
    list_products,
    get_product,
    add_product,
    modify_product,
    remove_product
)

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    products = list_products()
    products_list = [p.__dict__ for p in products]
    for p in products_list:
        p.pop('_sa_instance_state', None)
    return jsonify(products_list), 200

@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product_route(product_id):
    product = get_product(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    prod_dict = product.__dict__
    prod_dict.pop('_sa_instance_state', None)
    return jsonify(prod_dict), 200

@products_bp.route('/products', methods=['POST'])
def create_product_route():
    data = request.json
    if not data or not all(k in data for k in ('name', 'category', 'price', 'quantity')):
        return jsonify({'error': 'Bad request'}), 400
    product = add_product(data)
    prod_dict = product.__dict__
    prod_dict.pop('_sa_instance_state', None)
    return jsonify(prod_dict), 201

@products_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
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
def delete_product_route(product_id):
    product = remove_product(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify({'result': 'Product deleted'}), 200