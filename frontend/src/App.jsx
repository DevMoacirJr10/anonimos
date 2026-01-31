import React, { useState } from 'react';

function App() {
  // 1. Criando a "memória" para os campos (O que o usuário digita)
  const [emailLogin, setEmailLogin] = useState('');
  const [senhaLogin, setSenhaLogin] = useState('');
  const [nomeCad, setNomeCad] = useState('');
  const [emailCad, setEmailCad] = useState('');
  const [senhaCad, setSenhaCad] = useState('');

  const API_URL = "https://anonimos-wph7.onrender.com"; // Seu endereço no Render

  // 2. Função para o botão ENTRAR
  const handleLogin = async () => {
    const res = await fetch(`${API_URL}/testar_login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: emailLogin, senha: senhaLogin })
    });
    const dados = await res.json();
    alert(dados.mensagem || dados.detail);
  };

  // 3. Função para o botão CRIAR CONTA
  const handleCadastro = async () => {
    const res = await fetch(`${API_URL}/testar_cadastro`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome: nomeCad, email: emailCad, senha: senhaCad })
    });
    const dados = await res.json();
    alert(dados.mensagem || dados.detail);
  };

  return (
    <>
      <h1>Anônimos MMLNT</h1>

      <div className="login">
        <h2>Login Teste</h2>
        <label>Login: </label>
        <input type="text" value={emailLogin} onChange={(e) => setEmailLogin(e.target.value)} placeholder="E-mail" />
        <label>Senha: </label>
        <input type="password" value={senhaLogin} onChange={(e) => setSenhaLogin(e.target.value)} placeholder="Senha" />
        {/* AQUI ESTÁ A MUDANÇA: O onClick */}
        <button className="btn-login" onClick={handleLogin}>Entrar</button>
      </div>

      <div className="new-login">
        <h2>Criar Conta Teste</h2>
        <label>Usuário: </label>
        <input type="text" value={nomeCad} onChange={(e) => setNomeCad(e.target.value)} placeholder="Nome" />
        <label>E-mail: </label>
        <input type="email" value={emailCad} onChange={(e) => setEmailCad(e.target.value)} placeholder="E-mail" />
        <label>Senha: </label>
        <input type="password" value={senhaCad} onChange={(e) => setSenhaCad(e.target.value)} placeholder="Senha" />
        {/* AQUI TAMBÉM: O onClick */}
        <button className="btn-new-login" onClick={handleCadastro}>Criar Conta</button>
      </div>
    </>
  );
}

export default App;