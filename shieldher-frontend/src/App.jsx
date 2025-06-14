import React from "react";
import Navbar from "./navbar";
import "./App.css";

export default function App() {
  return (
    <div className="app">
      <Navbar />
      <div className="main-content">
        <h1>Welcome to ShieldHer</h1>
        <p>Your private space for online safety and support.</p>
      </div>
    </div>
  );
}
