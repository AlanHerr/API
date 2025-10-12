
"""
Servicio de usuarios: lógica de negocio para registro, autenticación y listado de usuarios.
Incluye funciones para registrar, autenticar y listar usuarios, así como el manejo seguro de contraseñas.
"""

from repository.user_repository import UserRepository
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    @staticmethod
    def register_user(username, password):
        """
        Registra un nuevo usuario si el username no existe.
        Almacena la contraseña de forma segura (hash).
        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña en texto plano.
        Returns:
            User | None: Instancia del usuario creado o None si ya existe.
        """
        if UserRepository.get_by_username(username):
            return None  # Usuario ya existe
        hashed_password = generate_password_hash(password)
        user = UserRepository.create_user(username, hashed_password)
        return user

    @staticmethod
    def authenticate(username, password):
        """
        Autentica un usuario verificando el hash de la contraseña.
        Devuelve el usuario si es válido, None si no.
        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña en texto plano.
        Returns:
            User | None: Instancia del usuario si la autenticación es exitosa, None si falla.
        """
        user = UserRepository.get_by_username(username)
        if user and check_password_hash(user.password, password):
            return user
        return None

    @staticmethod
    def list_users():
        """
        Devuelve la lista de todos los usuarios registrados.
        Returns:
            list: Lista de instancias User.
        """
        return UserRepository.get_all()
