
"""
Controlador de usuarios: define los endpoints REST para registro, login y listado de usuarios.
"""

"""
Controlador de usuarios: define los endpoints REST para registro, login y listado de usuarios.
El registro y login son públicos; el listado requiere JWT.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from service.user_service import UserService

# Crear blueprint para agrupar rutas de usuarios
users_bp = Blueprint('users', __name__)

@users_bp.route('/users/register', methods=['POST'])
def register():
    """
    Registrar un nuevo usuario (username único, contraseña hasheada).
    Recibe JSON con username y password.
    Devuelve mensaje de éxito o error si ya existe.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Username and password required'}), 400
    user = UserService.register_user(username, password)
    if not user:
        return jsonify({'error': 'User already exists'}), 409
    return jsonify({'message': 'User registered successfully'}), 201

@users_bp.route('/users/login', methods=['POST'])
def login():
    """
    Login de usuario. Devuelve un JWT si las credenciales son válidas.
    Recibe JSON con username y password.
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = UserService.authenticate(username, password)
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=str(user.id))
    return jsonify({'access_token': access_token}), 200

@users_bp.route('/users/', methods=['GET'])
@jwt_required()
def list_users():
    """
    Listar todos los usuarios registrados (requiere JWT).
    Devuelve lista de usuarios (id y username).
    """
    users = UserService.list_users()
    users_list = [ {'id': u.id, 'username': u.username} for u in users ]
    return jsonify(users_list), 200
