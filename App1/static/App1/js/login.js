document.addEventListener('DOMContentLoaded', () => {
    const loginButton = document.querySelector('form button');

    if (loginButton) {
        loginButton.addEventListener('click', () => {
            loginButton.innerHTML = 'Logging in...';
            loginButton.disabled = true;
        });
    }
});
