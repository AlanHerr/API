
# Servicio para convertir precios a diferentes monedas usando la API gratuita ExchangeRate-API
import requests
import logging

logger = logging.getLogger(__name__)

# URL de la API gratuita (sin necesidad de API key)
EXCHANGE_API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

def get_exchange_rates(base_currency='USD'):
    """
    Obtiene las tasas de cambio actuales desde la API externa.
    
    Args:
        base_currency (str): Moneda base (por defecto USD)
        
    Returns:
        dict: Diccionario con las tasas de cambio o None si hay error
    """
    try:
        url = EXCHANGE_API_URL.format(base_currency)
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        logger.info(f'Tasas de cambio obtenidas exitosamente para {base_currency}')
        return data
    except requests.exceptions.RequestException as e:
        logger.error(f'Error al obtener tasas de cambio: {str(e)}')
        return None

def convert_price(amount, from_currency='USD', to_currency='MXN'):
    """
    Convierte un monto de una moneda a otra.
    
    Args:
        amount (float): Cantidad a convertir
        from_currency (str): Moneda origen
        to_currency (str): Moneda destino
        
    Returns:
        dict: Resultado de la conversión o error
    """
    try:
        # Obtener tasas de cambio
        data = get_exchange_rates(from_currency)
        
        if not data:
            return {
                'error': 'No se pudo obtener las tasas de cambio',
                'success': False
            }
        
        # Verificar si la moneda destino existe
        if to_currency not in data.get('rates', {}):
            return {
                'error': f'Moneda {to_currency} no soportada',
                'success': False
            }
        
        # Realizar la conversión
        rate = data['rates'][to_currency]
        converted_amount = round(amount * rate, 2)
        
        return {
            'success': True,
            'original_amount': amount,
            'original_currency': from_currency,
            'converted_amount': converted_amount,
            'target_currency': to_currency,
            'exchange_rate': rate,
            'date': data.get('date', 'N/A')
        }
        
    except Exception as e:
        logger.error(f'Error en conversión de moneda: {str(e)}')
        return {
            'error': f'Error en la conversión: {str(e)}',
            'success': False
        }

def get_supported_currencies():
    """
    Obtiene la lista de monedas soportadas.
    
    Returns:
        dict: Lista de códigos de monedas disponibles
    """
    try:
        data = get_exchange_rates('USD')
        if data and 'rates' in data:
            currencies = list(data['rates'].keys())
            currencies.append('USD')  # Agregar USD a la lista
            return {
                'success': True,
                'currencies': sorted(currencies),
                'total': len(currencies)
            }
        return {
            'error': 'No se pudieron obtener las monedas',
            'success': False
        }
    except Exception as e:
        logger.error(f'Error al obtener monedas soportadas: {str(e)}')
        return {
            'error': str(e),
            'success': False
        }

def convert_product_prices(products, target_currency='MXN', base_currency='USD'):
    """
    Convierte los precios de una lista de productos a otra moneda.
    
    Args:
        products (list): Lista de productos con precios
        target_currency (str): Moneda destino
        base_currency (str): Moneda base de los precios
        
    Returns:
        dict: Lista de productos con precios convertidos
    """
    try:
        data = get_exchange_rates(base_currency)
        
        if not data or target_currency not in data.get('rates', {}):
            return {
                'error': 'No se pudo realizar la conversión',
                'success': False
            }
        
        rate = data['rates'][target_currency]
        converted_products = []
        
        for product in products:
            product_dict = product.__dict__ if hasattr(product, '__dict__') else product
            product_copy = product_dict.copy()
            product_copy.pop('_sa_instance_state', None)
            
            original_price = product_copy.get('price', 0)
            converted_price = round(original_price * rate, 2)
            
            product_copy['original_price'] = original_price
            product_copy['original_currency'] = base_currency
            product_copy['price'] = converted_price
            product_copy['currency'] = target_currency
            product_copy['exchange_rate'] = rate
            
            converted_products.append(product_copy)
        
        return {
            'success': True,
            'products': converted_products,
            'exchange_rate': rate,
            'from_currency': base_currency,
            'to_currency': target_currency,
            'date': data.get('date', 'N/A')
        }
        
    except Exception as e:
        logger.error(f'Error al convertir precios de productos: {str(e)}')
        return {
            'error': str(e),
            'success': False
        }
