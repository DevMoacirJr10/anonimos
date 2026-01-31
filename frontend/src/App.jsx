function App() {
  return (
    <>
      <h1>Anônimos MMLNT</h1>

      <div class="login">
        <h2>Login Teste</h2>
        <label for="user">Login: </label>
        <input
          type="text"
          id="user"
          placeholder="Digite seu usuário logado  "
        />
        <label for="password">Senha: </label>
        <input type="password" id="password" placeholder="Digite sua senha" />
        <button class="btn-login">Entrar</button>
      </div>

      <div class="new-login">
        <h2>Criar Conta Teste</h2>
        <label for="user">Usuário: </label>
        <input type="text" id="user" placeholder="Seu nome" />
        <label for="email">E-mail: </label>
        <input type="email" id="email" placeholder="E-mail" />
        <label for="new-password">Crie uma nova senha: </label>
        <input
          type="password"
          id="new-password"
          placeholder="Crie uma nova senha"
        />
        <label for="new-password">Confirme sua nova senha: </label>
        <input
          type="password"
          id="new-password"
          placeholder="Confirme sua nova senha"
        />
        <button class="btn-new-login">Criar Conta</button>
      </div>
    </>
  );
}

export default App;
