# API de Productos

Este proyecto es una API RESTful desarrollada con Flask y SQLAlchemy para la gestión de productos de una tienda. La base de datos principal está alojada en Railway (PostgreSQL), con opción de respaldo local en SQLite.

## Estructura del Proyecto

```
API/
├── app.py
├── config/
│   ├── __init__.py
│   └── database.py
├── controller/
│   ├── __init__.py
│   └── products_controller.py
├── model/
│   ├── __init__.py
│   └── products_models.py
├── repository/
│   ├── __init__.py
│   └── products_repository.py
├── service/
│   ├── __init__.py
│   └── products_service.py
├── .env
└── README.md
```

## Descripción de Carpetas y Archivos

- **app.py**: Punto de entrada de la aplicación Flask. Registra los endpoints y arranca el servidor.
- **config/database.py**: Configura la conexión a la base de datos y provee sesiones para interactuar con ella.
- **controller/products_controller.py**: Define los endpoints de la API para productos (GET, POST, PUT, DELETE).
- **model/products_models.py**: Define el modelo de datos `Product` (estructura de la tabla en la base de datos).
- **repository/products_repository.py**: Implementa la lógica de acceso a datos (consultas, inserciones, actualizaciones, eliminaciones).
- **service/products_service.py**: Orquesta la lógica de negocio, usando los métodos del repositorio.
- **.env**: Contiene la URI de la base de datos remota.

## Endpoints Principales

- `GET /products`: Lista todos los productos.
- `GET /products/<id>`: Obtiene un producto por ID.
- `POST /products`: Crea un producto nuevo.
- `PUT /products/<id>`: Actualiza un producto existente.
- `DELETE /products/<id>`: Elimina un producto.

## Ejemplo de Modelo de Producto

```python
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
```

## Variables de Entorno

Agrega tu URI de Railway en el archivo `.env`:

```
MYSQL_URI=postgresql://usuario:contraseña@host:puerto/nombre_db
```

## Cómo ejecutar

1. Instala las dependencias:
   ```bash
   pip install flask sqlalchemy psycopg2-binary python-dotenv
   ```
2. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

## Notas
- El proyecto está modularizado siguiendo buenas prácticas (modelo, repositorio, servicio, controlador).
- Si la conexión a Railway falla, se usa SQLite local como respaldo.
- Los endpoints devuelven respuestas en formato JSON.

---

**Autor:** AlanHerr
