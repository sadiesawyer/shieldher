import React from "react";
import "./Navbar.css";
import logo from "./assets/logo.png";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <img src={logo} alt="ShieldHer Logo" className="logo" />
        <span className="brand">ShieldHer</span>
      </div>
      <div className="navbar-right">
        <a href="#">Find Resources</a>
        <a href="#">Threat Scanner</a>
        <a href="#">Report Incident</a>
        <a href="#">Log In</a>
      </div>
    </nav>
  );
}
