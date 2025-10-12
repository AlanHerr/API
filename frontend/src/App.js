

/**
 * Componente principal de la aplicación React.
 * Gestiona la autenticación, navegación y renderizado de vistas principales.
 */
import React, { useState } from "react";
import Login from "./Login";
import Register from "./Register";
import Products from "./Products";
import "./App.css";

function App() {
  // Estado para el token JWT y la vista actual
  const [token, setToken] = useState("");
  const [view, setView] = useState("login");

  /**
   * Maneja el login exitoso guardando el token y mostrando la vista principal.
   * @param {string} jwt - Token JWT recibido tras autenticación
   */
  const handleLogin = (jwt) => {
    setToken(jwt);
    setView("home");
  };

  /**
   * Cierra la sesión y vuelve a la pantalla de login.
   */
  const handleLogout = () => {
    setToken("");
    setView("login");
  };

  /**
   * Barra de navegación superior para cambiar entre vistas CRUD.
   */
  const NavBar = () => (
    <nav>
      <button className={view === "home" ? "active" : ""} onClick={() => setView("home")}>Inicio</button>
      <button className={view === "add" ? "active" : ""} onClick={() => setView("add")}>Añadir producto</button>
      <button className={view === "edit" ? "active" : ""} onClick={() => setView("edit")}>Editar producto</button>
      <button className={view === "delete" ? "active" : ""} onClick={() => setView("delete")}>Eliminar producto</button>
      <button style={{ marginLeft: "auto" }} onClick={handleLogout}>Cerrar sesión</button>
    </nav>
  );

  // Renderizado condicional según autenticación y vista
  return (
    <div className="app-container">
      <h1>API de Productos</h1>
      {token ? (
        <>
          <NavBar />
          {view === "home" && <Products token={token} mode="view" />}
          {view === "add" && <Products token={token} mode="add" onBack={() => setView("home")} />}
          {view === "edit" && <Products token={token} mode="edit" onBack={() => setView("home")} />}
          {view === "delete" && <Products token={token} mode="delete" onBack={() => setView("home")} />}
        </>
      ) : view === "login" ? (
        <>
          <Login onLogin={handleLogin} />
          <p>
            ¿No tienes cuenta?{' '}
            <button onClick={() => setView("register")}>Regístrate</button>
          </p>
        </>
      ) : (
        <>
          <Register onRegister={() => setView("login")} />
          <p>
            ¿Ya tienes cuenta?{' '}
            <button onClick={() => setView("login")}>Inicia sesión</button>
          </p>
        </>
      )}
    </div>
  );
}

export default App;
