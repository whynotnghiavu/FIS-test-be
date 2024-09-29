document.addEventListener("DOMContentLoaded", function() {
    const loginBtn = document.getElementById('loginBtn');
    const registerBtn = document.getElementById('registerBtn');
    const authForm = document.getElementById('authForm');
    const submitAuth = document.getElementById('submitAuth');
    const commentForm = document.getElementById('commentForm');
    let isLoggedIn = false;
  
    loginBtn.addEventListener('click', function() {
      authForm.querySelector('h2').innerText = "Login";
      authForm.querySelector('button').innerText = "Login";
    });
  
    registerBtn.addEventListener('click', function() {
      authForm.querySelector('h2').innerText = "Register";
      authForm.querySelector('button').innerText = "Register";
    });
  
    submitAuth.addEventListener('click', function() {
      isLoggedIn = true;
      authForm.style.display = "none";
      // Simulate logging in by hiding the form
    });
  
    commentForm.addEventListener('submit', function(event) {
      event.preventDefault();
      if (isLoggedIn) {
        const textarea = commentForm.querySelector('textarea');
        if (textarea.value.trim() !== "") {
          const newComment = document.createElement('div');
          newComment.classList.add('comment');
          newComment.innerHTML = `
            <img src="avatar-placeholder.svg" alt="User" class="avatar">
            <div>
              <p class="font-semibold">Current User</p>
              <p>${textarea.value}</p>
            </div>
          `;
          commentForm.insertAdjacentElement('beforebegin', newComment);
          textarea.value = '';
        }
      } else {
        alert("You need to log in to post a comment.");
      }
    });
  });
  