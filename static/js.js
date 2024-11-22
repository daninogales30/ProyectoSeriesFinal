const frasesMotivadoras = [
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "No te detengas hasta sentirte orgulloso.",
    "La única forma de hacer un gran trabajo es amar lo que haces.",
    "El futuro pertenece a quienes creen en la belleza de sus sueños.",
    "El miedo es temporal. El arrepentimiento es para siempre.",
    "Cada día es una nueva oportunidad para cambiar tu vida.",
    "No te rindas. Las grandes cosas llevan tiempo.",
    "Si puedes soñarlo, puedes lograrlo.",
    "El único modo de hacer un gran trabajo es amar lo que haces.",
    "Los límites solo existen en tu mente."
];

const boton = document.getElementById("sonrisa");
const parrafo = document.getElementById("p_feliz");

boton.addEventListener("click", function (){
    let indiceAleatorio = Math.floor(Math.random() * frasesMotivadoras.length);
    parrafo.textContent = frasesMotivadoras[indiceAleatorio];
})