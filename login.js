function validateLogin() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username === '' || password === '') {
        alert('Username and password are required.');
        return false;
    }

    // Additional login validations can be added here

    return true;
}

function validateRegister() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;

    if (username === '' || email === '' || password === '' || confirmPassword === '') {
        alert('All fields are required.');
        return false;
    }

    if (password !== confirmPassword) {
        alert('Password and Confirm Password must match.');
        return false;
    }

    // Additional register validations can be added here

    return true;
}