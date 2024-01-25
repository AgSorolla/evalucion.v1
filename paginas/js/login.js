function validateLogin() {
    var username = document.getElementById('nombre').value;
    var password = document.getElementById('contraseña').value;

    if (username === '' || password === '') {
        alert('tiene que completar las casillas.');
        return false;
    }
    return true;
}

function validateRegister() {
    var username = document.getElementById('nombre').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('contraseña').value;
    var confirmPassword = document.getElementById('confirmar contraseña').value;

    if (username === '' || email === '' || password === '' || confirmPassword === '') {
        alert('todo tiene que ser completado.');
        return false;
    }

    if (password !== confirmPassword) {
        alert('las contyraseñas no son iguales');
        return false;
    }
    return true;
}