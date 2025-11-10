
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
│   ├── user_controller.py
│   └── currency_controller.py        # ⭐ NUEVO: Endpoints de conversión de monedas
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
│   ├── user_service.py
│   └── currency_service.py           # ⭐ NUEVO: Lógica de conversión de monedas
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
├── requirements-prod.txt
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



## Variables de Entorno (Backend)

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
DATABASE_URI=postgresql://usuario:contraseña@host:puerto/nombre_db
JWT_SECRET_KEY=tu_clave_secreta_jwt
```

- `DATABASE_URI`: URI de Railway PostgreSQL (o SQLite para desarrollo local).
- `JWT_SECRET_KEY`: Clave secreta para firmar los tokens JWT.

---

## Variables de Entorno (Frontend)

El frontend React puede tener su propio archivo `.env` dentro de la carpeta `frontend/` para definir variables de entorno específicas del cliente. Estas variables permiten configurar, por ejemplo, la URL de la API backend o claves públicas de servicios externos.

Ejemplo de `.env` en `frontend/`:

```
REACT_APP_API_URL=http://localhost:5000
REACT_APP_GOOGLE_MAPS_KEY=tu_clave_publica
```

**Notas:**
- Todas las variables deben comenzar con `REACT_APP_` para que React las reconozca.
- Nunca pongas datos sensibles o secretos privados en el `.env` del frontend, ya que el código es visible para el usuario final.

---

## Tabla de Endpoints

### Endpoints de Productos

| Método | Endpoint              | Descripción                        | Autenticación | Body/Params |
|--------|-----------------------|------------------------------------|---------------|-------------|
| GET    | /products             | Lista todos los productos          | JWT           | -           |
| GET    | /products/<id>        | Obtiene un producto por ID         | JWT           | -           |
| POST   | /products             | Crea un producto nuevo             | JWT           | `name`, `category`, `price`, `quantity` |
| PUT    | /products/<id>        | Actualiza un producto existente    | JWT           | `name`, `category`, `price`, `quantity` |
| DELETE | /products/<id>        | Elimina un producto                | JWT           | -           |

### Endpoints de Usuarios

| Método | Endpoint              | Descripción                        | Autenticación | Body/Params |
|--------|-----------------------|------------------------------------|---------------|-------------|
| POST   | /users/register       | Registra un nuevo usuario          | No            | `username`, `password` |
| POST   | /users/login          | Inicia sesión y devuelve JWT       | No            | `username`, `password` |
| GET    | /users/               | Lista todos los usuarios           | JWT           | -           |

### Endpoints de Conversión de Monedas ⭐ NUEVO

| Método | Endpoint              | Descripción                        | Autenticación | Body/Params |
|--------|-----------------------|------------------------------------|---------------|-------------|
| POST   | /currency/convert     | Convierte un monto entre monedas   | JWT           | `amount`, `from_currency`, `to_currency` |
| GET    | /currency/rates       | Obtiene tasas de cambio actuales   | JWT           | `?base_currency=XXX` (opcional) |
| GET    | /currency/supported   | Lista las 166 monedas soportadas   | JWT           | -           |
| GET    | /products/convert     | Lista productos con precios convertidos | JWT      | `?currency=XXX` (requerido), `?base_currency=XXX` (opcional) |

---

---

## 💱 Conversión de Monedas (Nueva Funcionalidad)

La API ahora está integrada con **ExchangeRate-API**, una API externa 100% gratuita que proporciona tasas de cambio en tiempo real para más de 160 monedas mundiales.

### 🎯 ¿Qué puedes hacer?

1. **Convertir montos** entre cualquier par de monedas (USD ↔ MXN, EUR ↔ JPY, etc.)
2. **Ver tasas de cambio** actualizadas diariamente desde cualquier moneda base
3. **Listar monedas soportadas** (166 monedas disponibles)
4. **Convertir precios de productos** automáticamente a la moneda del cliente

### 🌐 API Externa Utilizada

- **Servicio:** [ExchangeRate-API](https://www.exchangerate-api.com/)
- **Costo:** 100% GRATUITO (sin límites significativos)
- **Autenticación:** No requiere API key
- **Actualización:** Tasas actualizadas diariamente
- **Monedas:** 166 monedas (AED, AFN, ALL, AMD, ARS, AUD, BRL, CAD, CHF, CNY, EUR, GBP, INR, JPY, KRW, MXN, RUB, USD, ZAR, y más)

### 📝 Características Técnicas

- ✅ **Integración externa:** Consume API REST de terceros
- ✅ **Manejo de errores:** Timeout de 5 segundos, mensajes claros
- ✅ **Logging:** Registro detallado de operaciones
- ✅ **Respaldo:** Devuelve precio original si la conversión falla
- ✅ **Cache-friendly:** Diseñado para implementar cache futuro
- ✅ **RESTful:** Endpoints claros y semánticos

---

## 📚 Documentación Detallada de Endpoints de Conversión

### 1️⃣ POST /currency/convert

Convierte un monto específico de una moneda a otra.

**Request:**
```bash
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{
    "amount": 100,
    "from_currency": "USD",
    "to_currency": "MXN"
  }'
```

**Body Parameters:**
- `amount` (float, requerido): Cantidad a convertir
- `from_currency` (string, opcional): Moneda origen (default: USD)
- `to_currency` (string, opcional): Moneda destino (default: MXN)

**Response 200 OK:**
```json
{
  "success": true,
  "original_amount": 100.0,
  "original_currency": "USD",
  "converted_amount": 1850.0,
  "target_currency": "MXN",
  "exchange_rate": 18.5,
  "date": "2025-11-08"
}
```

**Response 400 Bad Request:**
```json
{
  "success": false,
  "error": "Moneda MXX no soportada"
}
```

**Ejemplos de uso:**
```bash
# USD a Pesos Mexicanos
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"amount": 100, "from_currency": "USD", "to_currency": "MXN"}'

# Euros a Dólares
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"amount": 50, "from_currency": "EUR", "to_currency": "USD"}'

# Pesos Mexicanos a Yenes Japoneses
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"amount": 5000, "from_currency": "MXN", "to_currency": "JPY"}'
```

---

### 2️⃣ GET /currency/rates

Obtiene todas las tasas de cambio actuales para una moneda base específica.

**Request:**
```bash
curl "http://localhost:5000/currency/rates?base_currency=USD" \
  -H "Authorization: Bearer $TOKEN"
```

**Query Parameters:**
- `base_currency` (string, opcional): Moneda base para las tasas (default: USD)

**Response 200 OK:**
```json
{
  "base": "USD",
  "date": "2025-11-08",
  "time_last_updated": 1699401600,
  "rates": {
    "AED": 3.67,
    "AFN": 70.5,
    "ALL": 92.8,
    "AMD": 387.0,
    "ARS": 350.0,
    "AUD": 1.53,
    "BRL": 4.98,
    "CAD": 1.37,
    "CHF": 0.88,
    "CNY": 7.24,
    "EUR": 0.865,
    "GBP": 0.761,
    "INR": 83.25,
    "JPY": 153.32,
    "KRW": 1315.0,
    "MXN": 18.5,
    "RUB": 92.5,
    "ZAR": 18.75,
    "...": "..."
  }
}
```

**Ejemplos de uso:**
```bash
# Tasas desde USD
curl "http://localhost:5000/currency/rates?base_currency=USD" \
  -H "Authorization: Bearer $TOKEN"

# Tasas desde EUR
curl "http://localhost:5000/currency/rates?base_currency=EUR" \
  -H "Authorization: Bearer $TOKEN"

# Tasas desde MXN
curl "http://localhost:5000/currency/rates?base_currency=MXN" \
  -H "Authorization: Bearer $TOKEN"
```

---

### 3️⃣ GET /currency/supported

Obtiene la lista completa de las 166 monedas soportadas por la API.

**Request:**
```bash
curl http://localhost:5000/currency/supported \
  -H "Authorization: Bearer $TOKEN"
```

**Response 200 OK:**
```json
{
  "success": true,
  "total": 166,
  "currencies": [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP",
    "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS",
    "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF",
    "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD",
    "JPY", "KES", "KGS", "KHR", "KID", "KMF", "KRW", "KWD", "KYD", "KZT",
    "...más monedas..."
  ]
}
```

**Monedas Populares Incluidas:**
- 🇺🇸 USD - Dólar Estadounidense
- 🇲🇽 MXN - Peso Mexicano
- 🇪🇺 EUR - Euro
- 🇬🇧 GBP - Libra Esterlina
- 🇯🇵 JPY - Yen Japonés
- 🇨🇦 CAD - Dólar Canadiense
- 🇦🇺 AUD - Dólar Australiano
- 🇨🇭 CHF - Franco Suizo
- 🇨🇳 CNY - Yuan Chino
- 🇮🇳 INR - Rupia India
- 🇧🇷 BRL - Real Brasileño
- 🇦🇷 ARS - Peso Argentino
- 🇰🇷 KRW - Won Surcoreano
- 🇷🇺 RUB - Rublo Ruso
- 🇿🇦 ZAR - Rand Sudafricano

---

### 4️⃣ GET /products/convert ⭐ ENDPOINT DESTACADO

Obtiene todos los productos de tu inventario con los precios convertidos automáticamente a la moneda especificada. **Este es el endpoint más poderoso** para e-commerce internacional.

**Request:**
```bash
curl "http://localhost:5000/products/convert?currency=EUR" \
  -H "Authorization: Bearer $TOKEN"
```

**Query Parameters:**
- `currency` (string, **requerido**): Moneda destino para la conversión
- `base_currency` (string, opcional): Moneda base de los precios (default: USD)

**Response 200 OK:**
```json
{
  "success": true,
  "from_currency": "USD",
  "to_currency": "EUR",
  "exchange_rate": 0.865,
  "date": "2025-11-08",
  "products": [
    {
      "id": 1,
      "name": "Laptop",
      "category": "Electronics",
      "quantity": 10,
      "original_price": 1200.0,
      "original_currency": "USD",
      "price": 1038.0,
      "currency": "EUR",
      "exchange_rate": 0.865
    },
    {
      "id": 2,
      "name": "Mouse",
      "category": "Electronics",
      "quantity": 50,
      "original_price": 25.0,
      "original_currency": "USD",
      "price": 21.62,
      "currency": "EUR",
      "exchange_rate": 0.865
    },
    {
      "id": 3,
      "name": "Keyboard",
      "category": "Electronics",
      "quantity": 30,
      "original_price": 75.0,
      "original_currency": "USD",
      "price": 64.88,
      "currency": "EUR",
      "exchange_rate": 0.865
    }
  ]
}
```

**Ejemplos de uso:**
```bash
# Ver productos en Pesos Mexicanos
curl "http://localhost:5000/products/convert?currency=MXN" \
  -H "Authorization: Bearer $TOKEN"

# Ver productos en Euros
curl "http://localhost:5000/products/convert?currency=EUR" \
  -H "Authorization: Bearer $TOKEN"

# Ver productos en Yenes Japoneses
curl "http://localhost:5000/products/convert?currency=JPY" \
  -H "Authorization: Bearer $TOKEN"

# Ver productos en Libras Esterlinas
curl "http://localhost:5000/products/convert?currency=GBP" \
  -H "Authorization: Bearer $TOKEN"

# Convertir desde EUR a USD
curl "http://localhost:5000/products/convert?currency=USD&base_currency=EUR" \
  -H "Authorization: Bearer $TOKEN"
```

**Casos de Uso Reales:**

1. **E-commerce Internacional:**
   ```javascript
   // Mostrar productos en la moneda del país del cliente
   const userCountry = getUserCountry(); // 'MX', 'ES', 'JP', etc.
   const currency = getCurrencyByCountry(userCountry); // 'MXN', 'EUR', 'JPY'
   const products = await fetch(`/products/convert?currency=${currency}`);
   ```

2. **Comparación de Precios:**
   ```bash
   # ¿Son más baratos los productos en USD o EUR?
   curl "http://localhost:5000/products/convert?currency=USD"
   curl "http://localhost:5000/products/convert?currency=EUR"
   ```

3. **Reportes Financieros:**
   ```bash
   # Calcular inventario total en moneda local
   curl "http://localhost:5000/products/convert?currency=MXN" | \
     jq '.products | map(.price * .quantity) | add'
   ```

---

## 🚀 Ejemplos Completos de Integración

### Ejemplo 1: Flujo Completo de Conversión

```bash
# 1. Login y obtener token
TOKEN=$(curl -s -X POST http://localhost:5000/users/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "test123"}' \
  | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")

# 2. Crear productos en USD (precio base)
curl -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Laptop", "category": "Electronics", "price": 1200, "quantity": 10}'

# 3. Ver productos en Pesos Mexicanos
curl "http://localhost:5000/products/convert?currency=MXN" \
  -H "Authorization: Bearer $TOKEN"
# Resultado: Laptop = $22,200 MXN

# 4. Ver productos en Euros
curl "http://localhost:5000/products/convert?currency=EUR" \
  -H "Authorization: Bearer $TOKEN"
# Resultado: Laptop = €1,038 EUR

# 5. Ver productos en Yenes
curl "http://localhost:5000/products/convert?currency=JPY" \
  -H "Authorization: Bearer $TOKEN"
# Resultado: Laptop = ¥183,984 JPY
```

### Ejemplo 2: Calculadora de Viajes

```bash
# ¿Cuánto dinero necesito para un viaje?
# Tengo $5,000 MXN, ¿cuántos USD son?
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"amount": 5000, "from_currency": "MXN", "to_currency": "USD"}'
# Resultado: ~$270 USD

# ¿Y cuántos Euros?
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"amount": 5000, "from_currency": "MXN", "to_currency": "EUR"}'
# Resultado: ~€234 EUR
```

### Ejemplo 3: Análisis de Mercado

```bash
# Ver tasas de cambio actuales para análisis
curl "http://localhost:5000/currency/rates?base_currency=USD" \
  -H "Authorization: Bearer $TOKEN" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print(f'Fecha: {data[\"date\"]}')
print(f'USD → MXN: {data[\"rates\"][\"MXN\"]}')
print(f'USD → EUR: {data[\"rates\"][\"EUR\"]}')
print(f'USD → JPY: {data[\"rates\"][\"JPY\"]}')
print(f'USD → GBP: {data[\"rates\"][\"GBP\"]}')
"
```

---

## 🎨 Casos de Uso y Beneficios

### Para E-commerce
- 🌍 **Ventas Internacionales:** Muestra precios en la moneda del cliente automáticamente
- 💰 **Competitividad:** Compara precios en diferentes mercados
- 📊 **Analytics:** Analiza ventas consolidadas en una sola moneda
- 🛒 **UX Mejorada:** Cliente ve precios en su moneda familiar

### Para Aplicaciones Financieras
- 💸 **Transferencias:** Calcula el monto exacto de transferencias internacionales
- 📈 **Portafolio:** Convierte inversiones a moneda base
- 🏦 **Banca:** Muestra saldos en múltiples monedas
- 📉 **Trading:** Compara valores en tiempo real

### Para Viajes y Turismo
- ✈️ **Presupuesto de Viaje:** Calcula costos en moneda local
- 🏨 **Reservas:** Muestra precios de hoteles en la moneda del usuario
- 🍽️ **Restaurantes:** Convierte menús a la moneda del turista
- 🛍️ **Shopping:** Compara precios entre países

---

## ⚙️ Configuración y Dependencias

### Dependencias Nuevas

La funcionalidad de conversión de monedas requiere la librería `requests` para consumir la API externa.

**requirements.txt** (desarrollo):
```
requests==2.32.4
# ... otras dependencias
```

**requirements-prod.txt** (producción):
```
Flask==3.1.2
Flask-JWT-Extended==4.7.1
SQLAlchemy==2.0.43
python-dotenv==1.1.1
psycopg2-binary==2.9.9
gunicorn==20.1.0
requests==2.32.4  # ⭐ NUEVA DEPENDENCIA
```

### Instalación

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
python -c "import requests; print('✅ requests instalado correctamente')"
```

---

## 🔒 Seguridad y Mejores Prácticas

### Timeout y Manejo de Errores

Todos los requests a la API externa tienen un **timeout de 5 segundos** para evitar bloqueos:

```python
response = requests.get(url, timeout=5)
```

Si la API externa falla:
- Se devuelve un error claro al cliente
- Se registra en logs para debugging
- Los precios originales se mantienen disponibles

### Rate Limiting

Aunque ExchangeRate-API es gratuita, considera:
- **Implementar cache:** Guardar tasas por 1-24 horas
- **Batch processing:** Convertir múltiples montos en una sola llamada
- **Fallback:** Tener tasas de respaldo en caso de fallo

### Recomendaciones de Producción

1. **Implementar Cache:** Redis o Memcached para tasas de cambio
2. **Monitoreo:** Alertas si la API externa falla más de X%
3. **Backup:** Base de datos con tasas históricas
4. **HTTPS:** Siempre usar HTTPS en producción
5. **Variables de Entorno:** No hardcodear URLs de APIs

---

## 📊 Métricas y Monitoreo

### Logging Implementado

El servicio de conversión registra todas las operaciones:

```python
logger.info(f'Tasas de cambio obtenidas exitosamente para {base_currency}')
logger.error(f'Error al obtener tasas de cambio: {str(e)}')
logger.error(f'Error en conversión de moneda: {str(e)}')
```

### Monitorear en Producción

Métricas clave a observar:
- ✅ Tasa de éxito de conversiones
- ⏱️ Latencia promedio de la API externa
- 🔄 Número de requests por hora/día
- ❌ Errores y tipos de errores
- 💰 Tasas de cambio más solicitadas

---

## Pruebas con curl_examples.sh

El archivo [`curl_examples.sh`](./curl_examples.sh) contiene ejemplos actualizados de cómo consumir **todos los endpoints** de la API usando `curl`, incluyendo:

### Ejemplos Incluidos (18 casos de prueba):

**Autenticación (1-2):**
- Registro de usuario
- Login y obtención de token JWT

**CRUD de Productos (3-10):**
- Listar todos los productos
- Obtener producto por ID (casos de éxito y error)
- Crear producto (casos de éxito y error)
- Actualizar producto (casos de éxito y error)
- Eliminar producto (casos de éxito y error)

**Conversión de Monedas (11-18) ⭐ NUEVO:**
- Convertir USD → MXN
- Convertir EUR → USD
- Obtener tasas de cambio base USD
- Obtener tasas de cambio base EUR
- Listar monedas soportadas
- Productos con precios en MXN
- Productos con precios en EUR
- Productos con precios en JPY

### Ejecutar los Ejemplos

```bash
# Dar permisos de ejecución
chmod +x curl_examples.sh

# Ejecutar todos los ejemplos
./curl_examples.sh

# O ejecutar comandos individuales
bash curl_examples.sh
```

### Personalizar los Ejemplos

Puedes modificar el archivo para:
- Cambiar las credenciales de usuario
- Ajustar los datos de productos
- Probar diferentes monedas
- Agregar tus propios casos de prueba

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

### Pruebas mínimas recomendadas

1. **Login con credenciales válidas:**
   - Espera un token JWT válido.
2. **Login con credenciales inválidas:**
   - Espera error 401.
3. **Acceso a ruta protegida sin token:**
   - Espera error 401.
4. **Acceso a ruta protegida con token válido:**
   - Espera respuesta exitosa.

---


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

---

## 🚀 Roadmap y Mejoras Futuras

### Conversión de Monedas v2.0

Posibles mejoras para la funcionalidad de conversión:

1. **Sistema de Cache:**
   - Implementar Redis para cachear tasas por 1-24 horas
   - Reducir llamadas a API externa y mejorar performance
   - Actualización automática en background

2. **Histórico de Tasas:**
   - Guardar tasas de cambio en base de datos
   - Gráficas de tendencias (últimos 7/30/90 días)
   - API para consultar tasas históricas

3. **Alertas de Moneda:**
   - Notificar cuando una tasa alcance cierto valor
   - Email/SMS cuando USD/MXN suba o baje X%
   - Alertas personalizadas por usuario

4. **Integración Frontend:**
   - Selector de moneda en React
   - Conversión en tiempo real en la UI
   - Preferencias de moneda por usuario
   - Banderas de países en selector

5. **Analytics y Reportes:**
   - Dashboard con tasas populares
   - Exportar reportes en PDF/Excel
   - Gráficas interactivas (Chart.js)
   - Comparativas entre monedas

6. **Múltiples Proveedores:**
   - Fallback a APIs alternativas
   - Comparar tasas entre proveedores
   - Seleccionar mejor tasa disponible

7. **Calculadora Avanzada:**
   - Calcular impuestos internacionales
   - Incluir comisiones de conversión
   - Costos de transferencia bancaria
   - Calculadora de propinas

### Otras Mejoras del Proyecto

- **Roles y Permisos:** Admin, Seller, Customer
- **Carrito de Compras:** Sistema de checkout completo
- **Pasarela de Pago:** Stripe, PayPal, MercadoPago
- **Imágenes de Productos:** Upload y almacenamiento (AWS S3)
- **Búsqueda Avanzada:** Filtros, ordenamiento, paginación
- **Reviews y Ratings:** Sistema de valoraciones
- **Wishlist:** Lista de deseos por usuario
- **Notificaciones:** Email/Push notifications
- **Multi-idioma:** i18n para español e inglés
- **Testing:** Unit tests y integration tests
- **CI/CD:** GitHub Actions para deploy automático
- **Docker Compose:** Orquestación completa
- **API Documentation:** Swagger/OpenAPI
- **Rate Limiting:** Protección contra abuso
- **Logs Centralizados:** ELK Stack o similar

---

**Autor:** AlanHerr
