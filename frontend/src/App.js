
import React, { useState } from "react";
import Login from "./Login";
import Register from "./Register";
import Products from "./Products";
import "./App.css";

function App() {
  const [token, setToken] = useState("");
  const [view, setView] = useState("login");

  const handleLogin = (jwt) => {
    setToken(jwt);
    setView("home");
  };

  const handleLogout = () => {
    setToken("");
    setView("login");
  };

  // Navegación superior
  const NavBar = () => (
    <nav>
      <button className={view === "home" ? "active" : ""} onClick={() => setView("home")}>Inicio</button>
      <button className={view === "add" ? "active" : ""} onClick={() => setView("add")}>Añadir producto</button>
      <button className={view === "edit" ? "active" : ""} onClick={() => setView("edit")}>Editar producto</button>
      <button className={view === "delete" ? "active" : ""} onClick={() => setView("delete")}>Eliminar producto</button>
      <button style={{ marginLeft: "auto" }} onClick={handleLogout}>Cerrar sesión</button>
    </nav>
  );

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
