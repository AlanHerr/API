
# 0. Registrar usuario y obtener token
curl -i -X POST http://localhost:5000/users/register \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario1", "password": "tu_contraseña"}'

TOKEN=$(curl -s -X POST http://localhost:5000/users/login \
  -H "Content-Type: application/json" \
  -d '{"username": "usuario1", "password": "tu_contraseña"}' | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")

# 1. Obtener todos los productos
curl -i http://localhost:5000/products \
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

echo "\n\n=== ENDPOINTS DE CONVERSIÓN DE MONEDAS ==="
echo "Estos endpoints consumen la API externa ExchangeRate-API para obtener tasas actualizadas\n"

# 11. Convertir $100 USD a Pesos Mexicanos (MXN)
# Resultado esperado: ~$1,850 MXN (1 USD ≈ 18.5 MXN)
echo "\n11. Convertir \$100 USD → MXN (Peso Mexicano)"
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"amount": 100, "from_currency": "USD", "to_currency": "MXN"}'

# 12. Convertir $1 USD a Pesos Colombianos (COP)
# Resultado esperado: ~3,780 COP (1 USD ≈ 3,780 COP)
echo "\n\n12. Convertir \$1 USD → COP (Peso Colombiano)"
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"amount": 1, "from_currency": "USD", "to_currency": "COP"}'

# 13. Convertir €50 EUR a Dólares (USD)
# Resultado esperado: ~$58 USD (1 EUR ≈ 1.16 USD)
echo "\n\n13. Convertir €50 EUR → USD (Dólar)"
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"amount": 50, "from_currency": "EUR", "to_currency": "USD"}'

# 14. Convertir $1000 COP a Dólares (USD)
# Resultado esperado: ~$0.26 USD
echo "\n\n14. Convertir 1000 COP → USD (conversión inversa)"
curl -X POST http://localhost:5000/currency/convert \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"amount": 1000, "from_currency": "COP", "to_currency": "USD"}'

# 15. Obtener tasas de cambio actuales (base USD)
# Muestra todas las tasas desde USD a las 166 monedas
echo "\n\n15. Obtener tasas de cambio actuales (base USD)"
curl http://localhost:5000/currency/rates \
  -H "Authorization: Bearer $TOKEN"

# 16. Obtener tasas de cambio con base EUR
# Muestra todas las tasas desde EUR
echo "\n\n16. Obtener tasas de cambio con base EUR"
curl "http://localhost:5000/currency/rates?base_currency=EUR" \
  -H "Authorization: Bearer $TOKEN"

# 17. Obtener lista de monedas soportadas
# Muestra las 166 monedas disponibles (AED, AFN, ALL, AMD, ARS, AUD, BRL, CAD, CHF, CNY, COP, EUR, GBP, INR, JPY, KRW, MXN, RUB, USD, ZAR, etc.)
echo "\n\n17. Obtener lista de monedas soportadas"
curl http://localhost:5000/currency/supported \
  -H "Authorization: Bearer $TOKEN"

# 18. Obtener todos los productos con precios en MXN
# Convierte automáticamente el precio de todos los productos de USD a MXN
echo "\n\n18. Obtener productos con precios en MXN"
curl "http://localhost:5000/products/convert?currency=MXN" \
  -H "Authorization: Bearer $TOKEN"

# 19. Obtener todos los productos con precios en EUR
# Convierte automáticamente el precio de todos los productos de USD a EUR
echo "\n\n19. Obtener productos con precios en EUR"
curl "http://localhost:5000/products/convert?currency=EUR" \
  -H "Authorization: Bearer $TOKEN"

# 20. Obtener productos con precios en COP
# Convierte automáticamente el precio de todos los productos de USD a Pesos Colombianos
echo "\n\n20. Obtener productos con precios en COP (Peso Colombiano)"
curl "http://localhost:5000/products/convert?currency=COP" \
  -H "Authorization: Bearer $TOKEN"

# 21. Obtener productos con precios en JPY (Yen Japonés)
echo "\n\n21. Obtener productos con precios en JPY (Yen Japonés)"
curl "http://localhost:5000/products/convert?currency=JPY&base_currency=USD" \
  -H "Authorization: Bearer $TOKEN"
