
# Importa la clase principal de Flask para crear la aplicación web
from flask import Flask
# Importa el blueprint de productos que contiene las rutas/endpoints
from controller.products_controller import products_bp

# Crea una instancia de la aplicación Flask
app = Flask(__name__)
# Registra el blueprint de productos en la aplicación principal
app.register_blueprint(products_bp)

# Si el archivo se ejecuta directamente, inicia el servidor Flask
if __name__ == '__main__':
    # Ejecuta la app en modo debug y en todas las interfaces de red
    app.run(debug=True, host='0.0.0.0')