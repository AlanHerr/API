
/**
 * Componente de formulario de registro de usuario.
 * Permite crear un nuevo usuario y muestra mensajes de éxito o error.
 * @param {function} onRegister - Callback tras registro exitoso
 */
import React, { useState } from "react";
import axios from "axios";

function Register({ onRegister }) {
  // Estados para usuario, contraseña, error y éxito
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  /**
   * Envía el formulario de registro y maneja la creación de usuario.
   */
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");
    try {
      await axios.post("/users/register", { username, password });
      setSuccess("Usuario registrado. Ahora puedes iniciar sesión.");
      setUsername("");
      setPassword("");
      onRegister();
    } catch (err) {
      setError("No se pudo registrar el usuario");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Registro</h2>
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
      <button type="submit">Registrarse</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {success && <p style={{ color: "green" }}>{success}</p>}
    </form>
  );
}

export default Register;
