const form = document.getElementById("loginForm");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const email = document.getElementById("login").value;
  const senha = document.getElementById("senha").value;

  try {
    const response = await fetch("http://127.0.0.1:8000/testar_login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        senha: senha,
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      alert(data.detail);
      return;
    }

    alert(data.mensagem);

    window.location.href = "home.html";
  } catch (error) {
    console.error(error);
    alert("Erro ao conectar com o servidor");
  }
});
