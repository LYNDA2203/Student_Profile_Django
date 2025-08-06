document.addEventListener('DOMContentLoaded', () => {
    const loginButton = document.querySelector('form button');

    if (loginButton) {
        loginButton.addEventListener('click', () => {
            loginButton.innerHTML = 'Logging in...';
            loginButton.disabled = true;
        });
    }


const logoutButton = document.querySelector('#logout-btn');
    if (logoutButton) {
        logoutButton.addEventListener('click', () => {
            logoutButton.innerHTML = 'Logging out...';
            logoutButton.disabled = true;
        });
    }
});
