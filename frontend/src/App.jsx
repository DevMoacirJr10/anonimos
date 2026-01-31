import React, { useState } from 'react'; // 1. Importamos o 'useState' para o React ter memória

function App() {
  // --- MEMÓRIA DO FORMULÁRIO DE LOGIN ---
  const [loginUser, setLoginUser] = useState('');
  const [loginPass, setLoginPass] = useState('');

  // --- MEMÓRIA DO FORMULÁRIO DE CADASTRO ---
  const [nome, setNome] = useState('');
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');

  const URL_API = "https://anonimos-wph7.onrender.com"; // Endereço do seu "garçom" (Backend)

  // 2. FUNÇÃO QUE CHAMA O LOGIN
  const fazerLogin = async () => {
    const resposta = await fetch(`${URL_API}/testar_login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: loginUser, senha: loginPass }) // Transforma em JSON
    });
    const dados = await resposta.json();
    alert(dados.mensagem || dados.detail); // Mostra o que o backend respondeu
  };

  // 3. FUNÇÃO QUE CHAMA O CADASTRO
  const fazerCadastro = async () => {
    const resposta = await fetch(`${URL_API}/testar_cadastro`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nome: nome, email: email, senha: senha })
    });
    const dados = await resposta.json();
    alert(dados.mensagem || dados.detail);
  };

  return (
    <>
      <h1>Anônimos MMLNT</h1>

      <div className="login">
        <h2>Login Teste</h2>
        <label htmlFor="user">Login: </label>
        <input 
          type="text" id="user" placeholder="Digite seu e-mail cadastrado" 
          value={loginUser} onChange={(e) => setLoginUser(e.target.value)} 
        />
        
        <label htmlFor="password">Senha: </label>
        <input 
          type="password" id="password" placeholder="Digite sua senha" 
          value={loginPass} onChange={(e) => setLoginPass(e.target.value)}
        />
        <button className="btn-login" onClick={fazerLogin}>Entrar</button>
      </div>

      <div className="new-login">
        <h2>Criar Conta Teste</h2>
        <label htmlFor="new-user">Usuário: </label>
        <input 
          type="text" id="new-user" placeholder="Seu nome" 
          value={nome} onChange={(e) => setNome(e.target.value)}
        />

        <label htmlFor="email">E-mail: </label>
        <input 
          type="email" id="email" placeholder="E-mail" 
          value={email} onChange={(e) => setEmail(e.target.value)}
        />

        <label htmlFor="new-password">Crie uma nova senha: </label>
        <input 
          type="password" id="new-password" placeholder="Crie uma nova senha" 
          value={senha} onChange={(e) => setSenha(e.target.value)}
        />

        <button className="btn-new-login" onClick={fazerCadastro}>Criar Conta</button>
      </div>
    </>
  );
}

export default App;