
# Controlador para endpoints de conversión de monedas
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from service.currency_service import (
    convert_price,
    get_supported_currencies,
    convert_product_prices
)
from service.products_service import list_products

# Crea un blueprint para agrupar las rutas relacionadas con conversión de monedas
currency_bp = Blueprint('currency', __name__)

@currency_bp.route('/currency/convert', methods=['POST'])
@jwt_required()
def convert_currency():
    """
    Convierte un monto de una moneda a otra.
    
    Body esperado:
    {
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "MXN"
    }
    """
    data = request.json
    
    # Validar datos requeridos
    if not data or 'amount' not in data:
        return jsonify({'error': 'El campo "amount" es requerido'}), 400
    
    try:
        amount = float(data['amount'])
    except (ValueError, TypeError):
        return jsonify({'error': 'El campo "amount" debe ser un número'}), 400
    
    from_currency = data.get('from_currency', 'USD').upper()
    to_currency = data.get('to_currency', 'MXN').upper()
    
    # Realizar conversión
    result = convert_price(amount, from_currency, to_currency)
    
    if result.get('success'):
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@currency_bp.route('/currency/rates', methods=['GET'])
@jwt_required()
def get_rates():
    """
    Obtiene las tasas de cambio actuales para una moneda base.
    
    Query params:
    - base_currency (opcional): Moneda base, por defecto USD
    """
    from service.currency_service import get_exchange_rates
    
    base_currency = request.args.get('base_currency', 'USD').upper()
    
    rates = get_exchange_rates(base_currency)
    
    if rates:
        return jsonify(rates), 200
    else:
        return jsonify({'error': 'No se pudieron obtener las tasas de cambio'}), 500

@currency_bp.route('/currency/supported', methods=['GET'])
@jwt_required()
def get_currencies():
    """
    Obtiene la lista de monedas soportadas por la API.
    """
    result = get_supported_currencies()
    
    if result.get('success'):
        return jsonify(result), 200
    else:
        return jsonify(result), 500

@currency_bp.route('/products/convert', methods=['GET'])
@jwt_required()
def convert_products_prices():
    """
    Obtiene todos los productos con precios convertidos a otra moneda.
    
    Query params:
    - currency (requerido): Moneda destino (ej: MXN, EUR, JPY)
    - base_currency (opcional): Moneda base de los precios, por defecto USD
    """
    target_currency = request.args.get('currency', '').upper()
    
    if not target_currency:
        return jsonify({'error': 'El parámetro "currency" es requerido'}), 400
    
    base_currency = request.args.get('base_currency', 'USD').upper()
    
    # Obtener todos los productos
    products = list_products()
    
    # Convertir precios
    result = convert_product_prices(products, target_currency, base_currency)
    
    if result.get('success'):
        return jsonify(result), 200
    else:
        return jsonify(result), 400
