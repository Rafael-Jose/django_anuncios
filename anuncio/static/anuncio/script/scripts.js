var hamburguer = document.querySelector(".hamburguer");

hamburguer.addEventListener("click", function () {
    document.querySelector(".menu-vertical").classList.toggle("show-menu");
});