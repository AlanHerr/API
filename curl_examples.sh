
# 0. Registrar usuario y obtener token
curl -i -X POST http://localhost:5000/users/register \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario1", "password": "tu_contraseña"}'

TOKEN=$(curl -s -X POST http://localhost:5000/users/login \
  -H "Content-Type: application/json" \
  -d '{"username": "Ender11", "password": "12345"}' | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")

# 1. Obtener todos los productos
echo "\n=== 1. Registro de usuario ==="
curl -i -X POST http://localhost:5000/users/register \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario1", "password": "tu_contraseña"}'

echo "\n=== 2. Login de usuario y obtención de token JWT ==="
TOKEN=$(curl -s -X POST http://localhost:5000/users/login \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario1", "password": "tu_contraseña"}' | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")
echo "Token: $TOKEN"

echo "\n=== 3. Listar todos los productos (requiere JWT) ==="
curl -i $API_URL/products \
  -H "Authorization: Bearer $TOKEN"

echo "\n=== 4. Obtener producto por ID (ejemplo: 1) ==="
curl -i $API_URL/products/1 \
  -H "Authorization: Bearer $TOKEN"

echo "\n=== 5. Obtener producto inexistente (ejemplo: 99) ==="
curl -i $API_URL/products/99 \
  -H "Authorization: Bearer $TOKEN"

echo "\n=== 6. Crear un nuevo producto ==="
curl -i -X POST $API_URL/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Tablet", "category": "Electronics", "price": 350, "quantity": 30}'

echo "\n=== 7. Crear producto con datos incompletos (debe fallar) ==="
curl -i -X POST $API_URL/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Watch", "category": "Accessories"}'

echo "\n=== 8. Actualizar producto existente (ejemplo: 1) ==="
curl -i -X PUT $API_URL/products/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Smartphone", "category": "Electronics", "price": 750, "quantity": 120}'

echo "\n=== 9. Actualizar producto inexistente (debe fallar) ==="
curl -i -X PUT $API_URL/products/99 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Unknown", "category": "Unknown", "price": 0, "quantity": 0}'

echo "\n=== 10. Eliminar producto existente (ejemplo: 1) ==="
curl -i -X DELETE $API_URL/products/1 \
  -H "Authorization: Bearer $TOKEN"

echo "\n=== 11. Eliminar producto inexistente (debe fallar) ==="
curl -i -X DELETE $API_URL/products/99 \
  -H "Authorization: Bearer $TOKEN"

echo "\n=== 12. Crear producto con cantidad cero ==="
curl -i -X POST $API_URL/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Jacket", "category": "Clothing", "price": 60, "quantity": 0}'

echo "\n=== 13. Listar todos los usuarios (requiere JWT) ==="
curl -i $API_URL/users/ \
  -H "Authorization: Bearer $TOKEN"

# 2. Obtener un producto por ID (ejemplo: 1)
curl -i http://localhost:5000/products/1 \
  -H "Authorization: Bearer $TOKEN"

# 3. Obtener un producto inexistente (ejemplo: 99)
curl -i http://localhost:5000/products/99 \
  -H "Authorization: Bearer $TOKEN"

# 4. Crear un nuevo producto
curl -i -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Tablet", "category": "Electronics", "price": 350, "quantity": 30}'

# 5. Crear un producto con datos incompletos
curl -i -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Watch", "category": "Accessories"}'

# 6. Actualizar un producto existente (ejemplo: 2)
curl -i -X PUT http://localhost:5000/products/2 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Smartphone", "category": "Electronics", "price": 750, "quantity": 120}'

# 7. Actualizar un producto inexistente (ejemplo: 99)
curl -i -X PUT http://localhost:5000/products/99 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Unknown", "category": "Unknown", "price": 0, "quantity": 0}'

# 8. Eliminar un producto existente (ejemplo: 3)
curl -i -X DELETE http://localhost:5000/products/2 \
  -H "Authorization: Bearer $TOKEN"

# 9. Eliminar un producto inexistente (ejemplo: 99)
curl -i -X DELETE http://localhost:5000/products/99 \
  -H "Authorization: Bearer $TOKEN"

# 10. Crear un producto con cantidad cero
curl -i -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Jacket", "category": "Clothing", "price": 60, "quantity": 0}'
