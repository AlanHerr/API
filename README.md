# API de Productos


# API de Productos
Este proyecto es una solución completa para la gestión de productos y usuarios de una tienda, compuesta por una API RESTful desarrollada con Flask y SQLAlchemy, autenticación JWT, y un frontend moderno en React. La base de datos principal está alojada en Railway (PostgreSQL), con opción de respaldo local en SQLite.

Las dependencias del backend están listadas en el archivo `requirements.txt`. Puedes instalar todas las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```


## Estructura del Proyecto

```
API/
├── app.py
├── config/
│   ├── __init__.py
│   └── database.py
├── controller/
│   ├── __init__.py
│   ├── products_controller.py
│   └── user_controller.py
├── model/
│   ├── __init__.py
│   ├── products_models.py
│   └── user.py
├── repository/
│   ├── __init__.py
│   ├── products_repository.py
│   └── user_repository.py
├── service/
│   ├── __init__.py
│   ├── products_service.py
│   └── user_service.py
├── frontend/
│   ├── package.json
│   ├── package-lock.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.js
│       ├── App.css
│       ├── index.js
│       ├── Login.js
│       ├── Register.js
│       ├── Products.js
│       └── setupProxy.js
├── .env
└── README.md
```


## Descripción de Carpetas y Archivos

- **app.py**: Punto de entrada de la aplicación Flask. Registra los endpoints y arranca el servidor.
- **config/database.py**: Configura la conexión a la base de datos y provee sesiones para interactuar con ella.
- **controller/products_controller.py**: Define los endpoints de la API para productos (GET, POST, PUT, DELETE).
- **controller/user_controller.py**: Define los endpoints de la API para usuarios (registro, login, listado).
- **model/products_models.py**: Define el modelo de datos `Product` (estructura de la tabla en la base de datos).
- **model/user.py**: Define el modelo de datos `User` (estructura de la tabla de usuarios).
- **repository/products_repository.py**: Implementa la lógica de acceso a datos de productos.
- **repository/user_repository.py**: Implementa la lógica de acceso a datos de usuarios.
- **service/products_service.py**: Orquesta la lógica de negocio de productos.
- **service/user_service.py**: Orquesta la lógica de negocio de usuarios y autenticación.
- **frontend/**: Aplicación React para la gestión visual de productos y usuarios.
   - **public/index.html**: HTML base de la app React.
   - **src/App.js**: Componente principal, navegación y autenticación.
   - **src/Products.js**: CRUD de productos y vistas.
   - **src/Login.js**: Formulario de login.
   - **src/Register.js**: Formulario de registro.
   - **src/App.css**: Estilos modernos y responsivos.
   - **src/setupProxy.js**: Proxy para desarrollo local.
- **.env**: Contiene la URI de la base de datos remota y otras variables sensibles.


## Endpoints Principales

### Productos
- `GET /products`: Lista todos los productos. (Requiere JWT)
- `GET /products/<id>`: Obtiene un producto por ID. (Requiere JWT)
- `POST /products`: Crea un producto nuevo. (Requiere JWT)
- `PUT /products/<id>`: Actualiza un producto existente. (Requiere JWT)
- `DELETE /products/<id>`: Elimina un producto. (Requiere JWT)

### Usuarios y Autenticación
- `POST /users/register`: Registra un nuevo usuario.
- `POST /users/login`: Inicia sesión y devuelve un token JWT.
- `GET /users/`: Lista todos los usuarios registrados. (Requiere JWT)


## Ejemplo de Modelos

### Producto
```python
class Product(Base):
   __tablename__ = 'products'
   id = Column(Integer, primary_key=True)
   name = Column(String(100), nullable=False)
   category = Column(String(50), nullable=False)
   price = Column(Float, nullable=False)
   quantity = Column(Integer, nullable=False)
```

### Usuario
```python
class User(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True)
   username = Column(String(80), unique=True, nullable=False)
   password = Column(String(255), nullable=False)
```


## Variables de Entorno

Agrega tu URI de Railway y la clave JWT en el archivo `.env`:

```
MYSQL_URI=postgresql://usuario:contraseña@host:puerto/nombre_db
JWT_SECRET_KEY=tu_clave_secreta_jwt
```


## Cómo ejecutar el backend
1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

## Cómo ejecutar el frontend
1. Entra a la carpeta del frontend:
   ```bash
   cd frontend
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Inicia la app React:
   ```bash
   npm start
   ```


## Notas
- El proyecto está modularizado siguiendo buenas prácticas (modelo, repositorio, servicio, controlador).
- Seguridad: Todos los endpoints sensibles están protegidos con JWT.
- Las contraseñas se almacenan de forma segura (hash).
- Si la conexión a Railway falla, se usa SQLite local como respaldo.
- El frontend React consume el API de forma segura y moderna.
- Los endpoints devuelven respuestas en formato JSON.
- No subas nunca la carpeta `node_modules/` al repositorio. Solo versiona el código fuente y los archivos de configuración (`package.json`, `package-lock.json`).

---

---

**Autor:** AlanHerr
