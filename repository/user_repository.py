
"""
Repositorio de usuarios: acceso a la base de datos para operaciones CRUD de usuarios.
Incluye funciones para buscar, crear y listar usuarios usando SQLAlchemy.
"""

from model.user import User
from config.database import get_db_session

class UserRepository:
    @staticmethod
    def get_by_username(username):
        """
        Busca un usuario por su username.
        Args:
            username (str): Nombre de usuario a buscar.
        Returns:
            User | None: Instancia del usuario o None si no existe.
        """
        session = get_db_session()
        user = session.query(User).filter_by(username=username).first()
        session.close()
        return user

    @staticmethod
    def create_user(username, hashed_password):
        """
        Crea un nuevo usuario con username y contraseña hasheada.
        Args:
            username (str): Nombre de usuario.
            hashed_password (str): Contraseña hasheada.
        Returns:
            User: Instancia del usuario creado.
        """
        session = get_db_session()
        user = User(username=username, password=hashed_password)
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()
        return user

    @staticmethod
    def get_all():
        """
        Devuelve la lista de todos los usuarios.
        Returns:
            list: Lista de instancias User.
        """
        session = get_db_session()
        users = session.query(User).all()
        session.close()
        return users
