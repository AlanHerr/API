

"""
Archivo principal de la aplicación Flask.
Registra los blueprints de productos y usuarios, configura JWT y arranca el servidor.
"""

import os
from flask import Flask
from controller.products_controller import products_bp  # Rutas de productos
from controller.user_controller import users_bp         # Rutas de usuarios
from flask_jwt_extended import JWTManager

# Crear instancia de la app Flask
app = Flask(__name__)

# Registrar blueprints para modularizar rutas
app.register_blueprint(products_bp)
app.register_blueprint(users_bp)

# Configuración de la clave secreta para JWT (puede venir de variable de entorno)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "tu_clave_secreta_jwt")

# Inicializar JWT
jwt = JWTManager(app)

if __name__ == '__main__':
    # Ejecutar la app en modo debug y accesible desde cualquier IP
    app.run(debug=True, host='0.0.0.0')