// togle active
const navbarnavbar = document.querySelector(".navbar-nav");
// di klik
document.querySelector("#menu").onclick = () => {
  navbarnavbar.classList.toggle("active");
};

// click luar hilang

const hambeger = document.querySelector("#menu");

document.addEventListener("click", function (e) {
  if (!hambeger.contains(e.target) && !navbarnavbar.contains(e.target)) {
    navbarnavbar.classList.remove("active");
  }
});
