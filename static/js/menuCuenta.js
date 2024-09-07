const menuToggle = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");
const icono = document.getElementById("icono");
const overlay = document.getElementById("overlay");

menuToggle.addEventListener("click", () => {
  // Cambia la posición del menú lateral al hacer clic en el botón
  if (sidebar.style.right === "-250px") {
    sidebar.style.right = "0";
    menuToggle.classList.add("active"); // Agrega la clase "active"
    icono.classList.add("bi-plus-lg");
    overlay.style.display = "block"; // Muestra la capa de fondo
  } else {
    sidebar.style.right = "-250px";
    menuToggle.classList.remove("active"); // Remueve la clase "active"
    icono.classList.remove("bi-plus-lg");
    overlay.style.display = "none"; // Oculta la capa de fondo
  }
});
