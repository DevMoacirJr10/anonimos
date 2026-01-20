// =====================
// BOTÃO
// =====================
const btn = document.querySelector(".btn-primary");
btn.addEventListener("mouseenter", () => 
    {
    gsap.to(btn, { scale: 1.1, duration: 0.2 });
    }
);
btn.addEventListener("mouseleave", () => 
    {
    gsap.to(btn, { scale: 1, duration: 0.2 });
    }
);
// =====================
// ENTRADA
// =====================
const input = document.querySelector(".input-text");

input.addEventListener("focus", () => 
    {
    gsap.to(input, 
        {
        borderColor: "#6a5cff",
        scale: 1.05,
        duration: 0.2
        });
    }
);

input.addEventListener("blur", () => 
    {
    gsap.to(input, 
        {
        borderColor: "#ccc",
        scale: 1,
        duration: 0.2
        });
    }
);

// =====================
// CARD
// =====================
const card = document.querySelector(".card");

card.addEventListener("mouseenter", () => 
    {
    gsap.to(card, 
        {
        y: -50,
        duration: 0.6,
        ease: "power2.out"
        });
    }
);
card.addEventListener("mouseleave", () => 
    {
    gsap.to(card, 
        {
        y: 0,
        duration: 0.3
        });
    }
);

// =====================
// SPUT FOGUETE
// =====================
const sput = document.querySelector(".sput-foguete");

let floatTween;
// Respiração idle (fica sempre)
gsap.to(sput, 
    {
    scale: 1.03,
    duration: 2,
    repeat: -1,
    yoyo: true,
    ease: "sine.inOut"
    }
);
sput.addEventListener("mouseenter", () => 
    {
    floatTween = gsap.to(sput, 
        {
        y: -50,
        rotation: 0,
        duration: 0.6,
        repeat: -1,
        yoyo: true,
        ease: "power1.inOut"
        });
    }
);
sput.addEventListener("mouseleave", () => 
    {
        floatTween.kill();
        gsap.to(sput, 
        {
        y: 0,
        rotation: 0,
        duration: 0.3,
        ease: "power2.out"
        });
    }
);