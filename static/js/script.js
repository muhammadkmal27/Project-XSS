let selectedImage = "";

// Daftar username yang telah terdaftar
let registeredUsers = [];

function toggleForm() {
  const registerForm = document.getElementById("register-form");
  const loginForm = document.getElementById("login-form");

  if (registerForm.style.display === "none") {
    registerForm.style.display = "block";
    loginForm.style.display = "none";
  } else {
    registerForm.style.display = "none";
    loginForm.style.display = "block";
  }
}

function selectSecurityImage(image, formId) {
  selectedImage = image;
  document.querySelectorAll(`#${formId} .image-grid img`).forEach((img) => {
    img.classList.remove("selected");
  });
  document
    .querySelector(`#${formId} img[src='${image}']`)
    .classList.add("selected");
}

function confirmSelection(formId) {
  if (formId === "register-form") {
    let username = document.getElementById("reg-username").value;
    let password = document.getElementById("reg-password").value;

    if (username && password && selectedImage) {
      if (registeredUsers.includes(username)) {
        alert(
          "Username is already registered. Please use a different username."
        );
      } else {
        localStorage.setItem("username", username);
        localStorage.setItem("password", password);
        localStorage.setItem("securityImage", selectedImage);
        registeredUsers.push(username); // Tambahkan username ke daftar terdaftar
        alert("Registration successful! Please select a security image.");
        // Tidak ada redirect karena masih di halaman register
      }
    } else {
      alert("Please fill in all fields and select a security image.");
    }
  } else if (formId === "login-form") {
    let storedUsername = localStorage.getItem("username");
    let storedPassword = localStorage.getItem("password");
    let storedSecurityImage = localStorage.getItem("securityImage");

    let username = document.getElementById("login-username").value;
    let password = document.getElementById("login-password").value;

    if (username === storedUsername && password === storedPassword) {
      if (selectedImage === storedSecurityImage) {
        alert("Login successful! You will be directed to the dashboard.");
        window.location.href = "dashboard.html"; // Arahkan ke halaman dashboard setelah login sukses
      } else {
        alert(
          "Your security image is incorrect. Please select the correct image."
        );
      }
    } else {
      alert("Username or password is incorrect.");
    }
  }
}

function register() {
  let username = document.getElementById("reg-username").value;
  let password = document.getElementById("reg-password").value;

  if (username && password && selectedImage) {
    if (registeredUsers.includes(username)) {
      alert("Username is already registered. Please use a different username.");
    } else {
      localStorage.setItem("username", username);
      localStorage.setItem("password", password);
      localStorage.setItem("securityImage", selectedImage);
      registeredUsers.push(username); // Tambahkan username ke daftar terdaftar
      alert("Registration successful! Please select a security image.");
      // Tidak ada redirect karena masih di halaman register
    }
  } else {
    alert("Please fill in all fields and select a security image.");
  }
}

function login() {
  let username = document.getElementById("login-username").value;
  let password = document.getElementById("login-password").value;

  let storedUsername = localStorage.getItem("username");
  let storedPassword = localStorage.getItem("password");
  let storedSecurityImage = localStorage.getItem("securityImage");

  if (username === storedUsername && password === storedPassword) {
    if (selectedImage === storedSecurityImage) {
      alert("Login successful! You will be directed to the dashboard.");
      window.location.href = "dashboard.html"; // Arahkan ke halaman dashboard setelah login sukses
    } else {
      alert(
        "Your security image is incorrect. Please select the correct image."
      );
    }
  } else {
    alert("Username or password is incorrect.");
  }
}

function logout() {
  window.location.href = "login_page.html"; // Arahkan kembali ke halaman login
}
