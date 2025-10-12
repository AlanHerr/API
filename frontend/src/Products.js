

/**
 * Componente para mostrar y gestionar productos.
 * Permite ver, añadir, editar y eliminar productos según el modo.
 * @param {string} token - JWT para autenticación
 * @param {string} mode - Modo de operación: 'view', 'add', 'edit', 'delete'
 * @param {function} onBack - Callback para volver a la vista principal
 */
import React, { useEffect, useState } from "react";
import axios from "axios";

function Products({ token, mode = "view", onBack }) {
  // Estados para productos, formularios, mensajes y carga
  const [products, setProducts] = useState([]);
  const [detail, setDetail] = useState(null);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [form, setForm] = useState({ name: "", category: "", price: "", quantity: "" });
  const [loading, setLoading] = useState(false);
  const [editId, setEditId] = useState(null);
  const [editForm, setEditForm] = useState({ name: "", category: "", price: "", quantity: "" });

  // Cargar productos al montar el componente
  useEffect(() => {
    fetchProducts();
  }, []);

  /**
   * Obtiene todos los productos de la API.
   */
  const fetchProducts = async () => {
    try {
      const res = await axios.get("/products", {
        headers: { Authorization: `Bearer ${token}` },
      });
      setProducts(res.data);
    } catch (err) {
      setError("No se pudieron cargar los productos");
    }
  };

  /**
   * Obtiene el detalle de un producto por ID.
   * @param {number} id - ID del producto
   */
  const fetchProductDetail = async (id) => {
    setError("");
    setSuccess("");
    try {
      const res = await axios.get(`/products/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setDetail(res.data);
    } catch (err) {
      setError("No se pudo obtener el detalle del producto");
    }
  };

  // Vista: Añadir producto
  if (mode === "add") {
    /**
     * Maneja cambios en el formulario de creación.
     */
    const handleChange = (e) => {
      setForm({ ...form, [e.target.name]: e.target.value });
    };
    /**
     * Envía el formulario para crear un producto.
     */
    const handleSubmit = async (e) => {
      e.preventDefault();
      setError("");
      setSuccess("");
      setLoading(true);
      try {
        await axios.post(
          "/products",
          {
            name: form.name,
            category: form.category,
            price: parseFloat(form.price),
            quantity: parseInt(form.quantity, 10),
          },
          {
            headers: { Authorization: `Bearer ${token}` },
          }
        );
        setSuccess("Producto creado exitosamente");
        setForm({ name: "", category: "", price: "", quantity: "" });
        fetchProducts();
      } catch (err) {
        setError("No se pudo crear el producto");
      } finally {
        setLoading(false);
      }
    };
    return (
      <div className="form-section">
        <h2>Añadir producto</h2>
        <form onSubmit={handleSubmit}>
          <input type="text" name="name" placeholder="Nombre" value={form.name} onChange={handleChange} required />
          <input type="text" name="category" placeholder="Categoría" value={form.category} onChange={handleChange} required />
          <input type="number" name="price" placeholder="Precio" value={form.price} onChange={handleChange} required min="0" step="0.01" />
          <input type="number" name="quantity" placeholder="Cantidad" value={form.quantity} onChange={handleChange} required min="0" />
          <button type="submit" disabled={loading}>{loading ? "Creando..." : "Crear"}</button>
          <button type="button" onClick={onBack}>Volver</button>
        </form>
        {error && <div className="error">{error}</div>}
        {success && <div className="success">{success}</div>}
      </div>
    );
  }

  // Vista: Editar producto
  if (mode === "edit") {
    /**
     * Permite editar productos en línea en la tabla.
     */
    return (
      <div>
        <h2>Editar producto</h2>
        <table className="products-table">
          <thead>
            <tr>
              <th>Nombre</th><th>Categoría</th><th>Precio</th><th>Cantidad</th><th>Acción</th>
            </tr>
          </thead>
          <tbody>
            {products.map((p) => (
              <tr key={p.id}>
                {editId === p.id ? (
                  <>
                    <td><input type="text" value={editForm.name} onChange={e => setEditForm({ ...editForm, name: e.target.value })} required /></td>
                    <td><input type="text" value={editForm.category} onChange={e => setEditForm({ ...editForm, category: e.target.value })} required /></td>
                    <td><input type="number" value={editForm.price} onChange={e => setEditForm({ ...editForm, price: e.target.value })} required min="0" step="0.01" /></td>
                    <td><input type="number" value={editForm.quantity} onChange={e => setEditForm({ ...editForm, quantity: e.target.value })} required min="0" /></td>
                    <td>
                      <button onClick={async () => {
                        setError(""); setSuccess("");
                        try {
                          await axios.put(`/products/${p.id}`, {
                            name: editForm.name,
                            category: editForm.category,
                            price: parseFloat(editForm.price),
                            quantity: parseInt(editForm.quantity, 10),
                          }, { headers: { Authorization: `Bearer ${token}` } });
                          setSuccess("Producto actualizado");
                          setEditId(null);
                          fetchProducts();
                        } catch {
                          setError("No se pudo actualizar el producto");
                        }
                      }}>Guardar</button>
                      <button onClick={() => setEditId(null)}>Cancelar</button>
                    </td>
                  </>
                ) : (
                  <>
                    <td>{p.name}</td>
                    <td>{p.category}</td>
                    <td>${p.price}</td>
                    <td>{p.quantity}</td>
                    <td>
                      <button onClick={() => {
                        setEditId(p.id);
                        setEditForm({ name: p.name, category: p.category, price: p.price, quantity: p.quantity });
                      }}>Editar</button>
                    </td>
                  </>
                )}
              </tr>
            ))}
          </tbody>
        </table>
        <button onClick={onBack}>Volver</button>
        {error && <div className="error">{error}</div>}
        {success && <div className="success">{success}</div>}
      </div>
    );
  }

  // Vista: Eliminar producto
  if (mode === "delete") {
    /**
     * Permite eliminar productos desde la tabla.
     */
    return (
      <div>
        <h2>Eliminar producto</h2>
        <table className="products-table">
          <thead>
            <tr>
              <th>Nombre</th><th>Categoría</th><th>Precio</th><th>Cantidad</th><th>Acción</th>
            </tr>
          </thead>
          <tbody>
            {products.map((p) => (
              <tr key={p.id}>
                <td>{p.name}</td>
                <td>{p.category}</td>
                <td>${p.price}</td>
                <td>{p.quantity}</td>
                <td>
                  <button style={{ background: '#d32f2f' }} onClick={async () => {
                    setError(""); setSuccess("");
                    try {
                      await axios.delete(`/products/${p.id}`, { headers: { Authorization: `Bearer ${token}` } });
                      setSuccess("Producto eliminado");
                      fetchProducts();
                    } catch {
                      setError("No se pudo eliminar el producto");
                    }
                  }}>Eliminar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <button onClick={onBack}>Volver</button>
        {error && <div className="error">{error}</div>}
        {success && <div className="success">{success}</div>}
      </div>
    );
  }

  // Vista: Inicio (tabla de productos y detalle)
  return (
    <div>
      <h2>Productos</h2>
      {detail && (
        <div className="form-section">
          <h3>Detalle del producto</h3>
          <p><b>ID:</b> {detail.id}</p>
          <p><b>Nombre:</b> {detail.name}</p>
          <p><b>Categoría:</b> {detail.category}</p>
          <p><b>Precio:</b> ${detail.price}</p>
          <p><b>Cantidad:</b> {detail.quantity}</p>
          <button onClick={() => setDetail(null)}>Cerrar</button>
        </div>
      )}
      <table className="products-table">
        <thead>
          <tr>
            <th>Nombre</th><th>Categoría</th><th>Precio</th><th>Cantidad</th><th>Detalle</th>
          </tr>
        </thead>
        <tbody>
          {products.map((p) => (
            <tr key={p.id}>
              <td>{p.name}</td>
              <td>{p.category}</td>
              <td>${p.price}</td>
              <td>{p.quantity}</td>
              <td>
                <button style={{ background: '#1976d2' }} onClick={() => fetchProductDetail(p.id)}>Ver detalle</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {error && <div className="error">{error}</div>}
      {success && <div className="success">{success}</div>}
    </div>
  );
}

export default Products;
