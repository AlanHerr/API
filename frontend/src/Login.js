
/**
 * Componente de formulario de inicio de sesión.
 * Permite al usuario autenticarse y obtener un token JWT.
 * @param {function} onLogin - Callback que recibe el token JWT tras login exitoso
 */
import React, { useState } from "react";
import axios from "axios";

function Login({ onLogin }) {
  // Estados para usuario, contraseña y error
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  /**
   * Envía el formulario de login y maneja la autenticación.
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const res = await axios.post("/users/login", { username, password });
      onLogin(res.data.access_token);
    } catch (err) {
      setError("Credenciales inválidas");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Iniciar sesión</h2>
      <input
        type="text"
        placeholder="Usuario"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button type="submit">Entrar</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </form>
  );
}

export default Login;
