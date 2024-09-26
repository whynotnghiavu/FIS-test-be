const loginBtn = document.getElementById("login-btn");
const registerBtn = document.getElementById("register-btn");
const logoutBtn = document.getElementById("logout-btn");
const authForm = document.getElementById("auth-form");
const commentForm = document.getElementById("comment-form");
const confirmPasswordField = document.getElementById("confirm-password");
const formTitle = document.getElementById("form-title");
const authSubmitBtn = document.getElementById("auth-submit-btn");

let isLoggedIn = false;
let isRegister = false;

function toggleAuthForm() {
    if (isRegister) {
        formTitle.textContent = "Register";
        confirmPasswordField.classList.remove("hidden");
        authSubmitBtn.textContent = "Register";
    } else {
        formTitle.textContent = "Login";
        confirmPasswordField.classList.add("hidden");
        authSubmitBtn.textContent = "Login";
    }
}

loginBtn.addEventListener("click", () => {
    isRegister = false;
    toggleAuthForm();
    authForm.classList.remove("hidden");
});

registerBtn.addEventListener("click", () => {
    isRegister = true;
    toggleAuthForm();
    authForm.classList.remove("hidden");
});

authSubmitBtn.addEventListener("click", () => {
    isLoggedIn = true;
    authForm.classList.add("hidden");
    logoutBtn.classList.remove("hidden");
    loginBtn.classList.add("hidden");
    registerBtn.classList.add("hidden");
    commentForm.classList.remove("hidden");
});

logoutBtn.addEventListener("click", () => {
    isLoggedIn = false;
    logoutBtn.classList.add("hidden");
    loginBtn.classList.remove("hidden");
    registerBtn.classList.remove("hidden");
    commentForm.classList.add("hidden");
});
