import React, { useState } from 'react';
import axios from 'axios';

const LoginForm = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    const params = new URLSearchParams();
    params.append("grant_type", "password");
    params.append("username", email);
    params.append("password", password);

    const response = await axios.post('http://localhost:8000/login', params, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });

    onLogin(response.data); // stocker token ou autre
  } catch (err) {
    console.error("Erreur login :", err.response?.data || err.message);
    setError("Email ou mot de passe invalide");
  }
};



  return (
    <form onSubmit={handleSubmit} className="max-w-sm mx-auto p-4 bg-white rounded shadow">
      <h2 className="text-xl font-bold mb-4">Connexion</h2>
      {error && <p className="text-red-500 text-sm mb-2">{error}</p>}
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        className="w-full mb-2 px-3 py-2 border rounded"
        required
      />
      <input
        type="password"
        placeholder="Mot de passe"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="w-full mb-4 px-3 py-2 border rounded"
        required
      />
      <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">Se connecter</button>
    </form>
  );
};

export default LoginForm;