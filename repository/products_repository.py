

"""
Repositorio de productos: acceso a la base de datos para operaciones CRUD de productos.
Proporciona funciones para listar, obtener, crear, actualizar y eliminar productos usando SQLAlchemy.
"""

from model.products_models import Product
from config.database import get_db_session

def get_all_products():
    """
    Devuelve todos los productos de la base de datos.
    Returns:
        list: Lista de instancias Product.
    """
    session = get_db_session()
    products = session.query(Product).all()
    session.close()
    return products

def get_product_by_id(product_id):
    """
    Devuelve un producto por su ID, o None si no existe.
    Args:
        product_id (int): ID del producto.
    Returns:
        Product | None: Instancia del producto o None si no existe.
    """
    session = get_db_session()
    product = session.query(Product).filter_by(id=product_id).first()
    session.close()
    return product

def create_product(data):
    """
    Crea un nuevo producto con los datos recibidos (dict).
    Args:
        data (dict): Diccionario con los datos del producto.
    Returns:
        Product: Instancia del producto creado.
    """
    session = get_db_session()
    product = Product(**data)
    session.add(product)
    session.commit()
    session.refresh(product)
    session.close()
    return product

def update_product(product_id, data):
    """
    Actualiza los datos de un producto existente por ID.
    Args:
        product_id (int): ID del producto a actualizar.
        data (dict): Campos a modificar.
    Returns:
        Product | None: Instancia del producto actualizado o None si no existe.
    """
    session = get_db_session()
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        for key, value in data.items():
            setattr(product, key, value)
        session.commit()
        session.refresh(product)
    session.close()
    return product

def delete_product(product_id):
    """
    Elimina un producto de la base de datos por ID.
    Args:
        product_id (int): ID del producto a eliminar.
    Returns:
        Product | None: Instancia del producto eliminado o None si no existe.
    """
    session = get_db_session()
    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        session.delete(product)
        session.commit()
    session.close()
    return product