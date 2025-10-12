
# API de Productos

Proyecto integral para la gestión de productos y usuarios de una tienda, compuesto por:
- **Backend:** API RESTful con Flask, SQLAlchemy y autenticación JWT.
- **Frontend:** React moderno y responsivo.
- **Base de datos:** PostgreSQL (Railway) y respaldo local SQLite.

---

## Tabla de Contenidos
1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Instalación y Ejecución](#instalación-y-ejecución)
3. [Variables de Entorno](#variables-de-entorno)
4. [Tabla de Endpoints](#tabla-de-endpoints)
5. [Pruebas con curl_examples.sh](#pruebas-con-curlexamplessh)
6. [Notas de Seguridad y Roles](#notas-de-seguridad-y-roles)
7. [Testing y Buenas Prácticas](#testing-y-buenas-prácticas)
8. [Autor](#autor)

---

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
├── requirements.txt
├── curl_examples.sh
└── README.md
```

---

## Instalación y Ejecución


### Backend (API Flask)
1. **Crea y activa un entorno virtual (.venv):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura las variables de entorno (ver sección abajo).
4. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

### Frontend (React)
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

---

## Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
DATABASE_URI=postgresql://usuario:contraseña@host:puerto/nombre_db
JWT_SECRET_KEY=tu_clave_secreta_jwt
```

- `DATABASE_URI`: URI de Railway PostgreSQL (o SQLite para desarrollo local).
- `JWT_SECRET_KEY`: Clave secreta para firmar los tokens JWT.

---

## Tabla de Endpoints

| Método | Endpoint              | Descripción                        | Autenticación |
|--------|-----------------------|------------------------------------|---------------|
| GET    | /products             | Lista todos los productos          | JWT           |
| GET    | /products/<id>        | Obtiene un producto por ID         | JWT           |
| POST   | /products             | Crea un producto nuevo             | JWT           |
| PUT    | /products/<id>        | Actualiza un producto existente    | JWT           |
| DELETE | /products/<id>        | Elimina un producto                | JWT           |
| POST   | /users/register       | Registra un nuevo usuario          | No            |
| POST   | /users/login          | Inicia sesión y devuelve JWT       | No            |
| GET    | /users/               | Lista todos los usuarios           | JWT           |

---

## Pruebas con curl_examples.sh

El archivo [`curl_examples.sh`](./curl_examples.sh) contiene ejemplos de cómo consumir todos los endpoints de la API usando `curl`, incluyendo:
- Registro y login de usuario
- Obtención de token JWT
- CRUD de productos (casos de éxito y error)

Para ejecutar los ejemplos:
```bash
chmod +x curl_examples.sh
./curl_examples.sh
```

Puedes modificar los datos de ejemplo según tus necesidades.

---

## Notas de Seguridad y Roles

- **Roles:** Actualmente todos los usuarios registrados pueden acceder a los endpoints protegidos (no hay distinción de roles).
- **JWT:** Todos los endpoints de productos y el listado de usuarios requieren autenticación JWT.
- **Contraseñas:** Se almacenan de forma segura (hash).
- **Variables sensibles:** No subas `.env` ni credenciales al repositorio.
- **Base de datos:** Si la conexión a Railway falla, se usa SQLite local como respaldo.

---

## Testing y Buenas Prácticas

- El backend y frontend están modularizados siguiendo buenas prácticas (modelo, repositorio, servicio, controlador).
- El frontend React permite probar todos los endpoints de la API de forma visual.
- Puedes probar la API sin frontend usando el archivo [`curl_examples.sh`](./curl_examples.sh).
- Los endpoints devuelven respuestas en formato JSON.
- Para pruebas automáticas, puedes usar herramientas como Postman, Insomnia o pytest.

---

## Autor

AlanHerr
