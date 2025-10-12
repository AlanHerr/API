

"""
Servicio de productos: lógica de negocio para CRUD de productos.
"""

from repository.products_repository import (
    get_all_products,
    """
    create_product,
    update_product,
    delete_product
    # Importar funciones del repositorio de productos
)

def list_products():
    """
    Devuelve la lista de todos los productos.
    """
    return get_all_products()

def get_product(product_id):
    """
    Devuelve un producto por su ID.
    """
    return get_product_by_id(product_id)

def add_product(data):
    """
    Agrega un nuevo producto con los datos recibidos.
    """
    return create_product(data)

def modify_product(product_id, data):
    """
    Modifica un producto existente con los datos recibidos.
    """
    return update_product(product_id, data)

def remove_product(product_id):
    """
    Elimina un producto por su ID.
    """
    return delete_product(product_id)