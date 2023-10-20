function checkPasswords(passwordField1, passwordField2, errorField) {
    const password = passwordField1.value;
    const password2 = passwordField2.value;

    if (password === password2 || password2 === '') {
        errorField.textContent = '';
    } else {
        errorField.textContent = 'Passwords do not match';
    }
}

document.addEventListener("DOMContentLoaded", function () {
    // Form error
    try {
        form_errors = document.querySelector('.register-datas').dataset.errors;
        for (const [key, value] of Object.entries(form_errors)) {
            const errorField = document.getElementById(key + '_errors');
            errorField.textContent = value.join(' ');
        }
    } catch { }

    // Passwords match check
    const passwordField = document.getElementById('password');
    const password2Field = document.getElementById('password2');

    const errorField = document.getElementById('error-field');

    passwordField.addEventListener(
        'input', () => checkPasswords(passwordField, password2Field, errorField)
    );
    password2Field.addEventListener(
        'input', () => checkPasswords(passwordField, password2Field, errorField)
    );
});