/* global gsap */
// Animação suave dos planetas
gsap.utils.toArray(".planet").forEach((planet, i) => {
  gsap.to(planet, {
    y: "+=15",
    duration: 2 + i * 0.3,
    repeat: -1,
    yoyo: true,
    ease: "sine.inOut"
  });
});

// Sol pulsando
gsap.to(".sun", {
  scale: 1.05,
  duration: 3,
  repeat: -1,
  yoyo: true,
  ease: "sine.inOut"
});
// Animação do cometa
const comet = document.querySelector(".comet");

function flyComet() {
  gsap.fromTo(
    comet,
    {
      x: -300,
      y: -200,
      rotation: -95,
      opacity: 1
    },
    {
      x: 1900,
      y: 900,
      rotation: -95,
      duration: 5,
      ease: "power2.inOut",
      onComplete: () => {
        gsap.set(comet, { opacity: 0 });
        setTimeout(() => {
          gsap.set(comet, { opacity: 1 });
          flyComet();
        }, 1500); // tempo até o próximo cometa
      }
    }
  );
}
flyComet();