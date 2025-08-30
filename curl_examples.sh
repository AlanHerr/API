# 1. Obtener todos los productos
curl -i http://localhost:5000/products

# 2. Obtener un producto por ID (ejemplo: 1)
curl -i http://localhost:5000/products/1

# 3. Obtener un producto inexistente (ejemplo: 99)
curl -i http://localhost:5000/products/99

# 4. Crear un nuevo producto
curl -i -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Tablet", "category": "Electronics", "price": 350, "quantity": 30}'

# 5. Crear un producto con datos incompletos
curl -i -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Watch", "category": "Accessories"}'

# 6. Actualizar un producto existente (ejemplo: 2)
curl -i -X PUT http://localhost:5000/products/2 \
  -H "Content-Type: application/json" \
  -d '{"name": "Smartphone", "category": "Electronics", "price": 750, "quantity": 120}'

# 7. Actualizar un producto inexistente (ejemplo: 99)
curl -i -X PUT http://localhost:5000/products/99 \
  -H "Content-Type: application/json" \
  -d '{"name": "Unknown", "category": "Unknown", "price": 0, "quantity": 0}'

# 8. Eliminar un producto existente (ejemplo: 3)
curl -i -X DELETE http://localhost:5000/products/3

# 9. Eliminar un producto inexistente (ejemplo: 99)
curl -i -X DELETE http://localhost:5000/products/99

# 10. Crear un producto con cantidad cero
curl -i -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Jacket", "category": "Clothing", "price": 60, "quantity": 0}'
