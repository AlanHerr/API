
"""
Modelo de datos para usuarios.
Define la clase User para la tabla de usuarios en la base de datos.
"""

from sqlalchemy import Column, Integer, String
from model.products_models import Base

class User(Base):
    """
    Modelo User: representa un usuario en la base de datos.
    Atributos:
        id (int): ID primario.
        username (str): Nombre de usuario único.
        password (str): Contraseña hasheada.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)  # ID único del usuario
    username = Column(String(80), unique=True, nullable=False)  # Nombre de usuario único
    password = Column(String(255), nullable=False)  # Contraseña hasheada

    def __repr__(self):
        return f'<User {self.username}>'
