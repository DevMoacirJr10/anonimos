/* global gsap */
window.addEventListener("load", () => {
  const imgElement = document.querySelector(".luminho-png");
  const totalFrames = 16;
  const frames = [];

  for (let i = 1; i <= totalFrames; i++) {
    let num = i.toString().padStart(2, "0");
    frames.push(`assets/img/luminho comemorando (${num}).png`);
  }

  let aniObj = { frame: 0 };
  gsap.to(aniObj, {
    frame: totalFrames - 1,
    snap: "frame",
    repeat: -1,
    duration: 1.5,
    ease: "none",
    onUpdate: () => {
      imgElement.src = frames[aniObj.frame];
    },
  });

  const tl = gsap.timeline();

  tl.to(".arrow-reveal", {
    x: "500%",
    duration: 1.3,
    ease: "power2.inOut",
  })
    .to(
      ".logo-name1",
      {
        opacity: 1,
        duration: 0.5,
      },
      "-=1.2",
    )
    .set(".arrow-reveal", { display: "none" })
    .from(
      ".logo-name2",
      {
        y: 20,
        opacity: 0,
        duration: 0.8,
        ease: "back.out(1.7)",
      },
      "-=0.2",
    );

  gsap.to(".luminho-png", {
    y: -30,
    duration: 1.5,
    ease: "power1.inOut",
    repeat: -1,
    yoyo: true,
  });
});

window.addEventListener("load", () => {
  const prepararTexto = (seletor) => {
    const el = document.querySelector(seletor);
    const texto = el.innerText;
    el.innerHTML = "";
    texto.split("").forEach((letra) => {
      const span = document.createElement("span");
      span.innerHTML = letra === " " ? "&nbsp;" : letra;
      el.appendChild(span);
    });
  };

  prepararTexto(".logo-name1");
  prepararTexto(".logo-name2");

  gsap.to(".logo-name1 span, .logo-name2 span", {
    y: -20,
    scale: 1,
    duration: 0.6,
    repeat: -1,
    yoyo: true,
    ease: "sine.inOut",
    stagger: {
      each: 0.1,
      from: "start",
    },
  });
});
