// Login!

const loginForm = document.querySelector('.loginForm');

loginForm.onsubmit = function(){

    const url = 'http://127.0.0.1:8000/home';
    const username = document.querySelector('.usernameForm').value;
    const password = document.querySelector('.passwordForm').value;

    fetch('/login', {
        method: 'POST',
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => {
        if(response.status == 201)
            window.location.replace(url);//redirecting to the main page in case the user is loged in successfully
        else{
            alert("Invalid Username of Password");
        }
    })


   return false;
}
