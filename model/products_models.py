
"""
Modelo de datos para productos.
Define la clase Product para la tabla de productos en la base de datos.
"""

# Importa los tipos de columna y datos para definir la estructura de la tabla
from sqlalchemy import Column, Integer, String, Float
# Importa la función para crear la clase base de los modelos
from sqlalchemy.ext.declarative import declarative_base

# Crea la clase base para todos los modelos de la base de datos
Base = declarative_base()

class Product(Base):
    """
    Modelo Product: representa un producto en la base de datos.
    Atributos:
        id (int): ID primario.
        name (str): Nombre del producto.
        category (str): Categoría del producto.
        price (float): Precio del producto.
        quantity (int): Cantidad disponible.
    """
    __tablename__ = 'products'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)  # ID único del producto
    name = Column(String(100), nullable=False)  # Nombre del producto
    category = Column(String(50), nullable=False)  # Categoría del producto
    price = Column(Float, nullable=False)  # Precio del producto
    quantity = Column(Integer, nullable=False)  # Cantidad disponible