document.addEventListener('DOMContentLoaded', () => {
    const registerBtn = document.querySelector('.btn-success');

    if (registerBtn) {
        const courseNames = registerBtn.dataset.courses || "Courses Registered";

        registerBtn.addEventListener('mouseover', () => {
            registerBtn.textContent = 'Let\'s Go ';
        });

        registerBtn.addEventListener('mouseout', () => {
            registerBtn.textContent = 'Register for Courses';
        });

        registerBtn.addEventListener('click', () => {
            registerBtn.classList.add('clicked');
            registerBtn.textContent = `Registered: ${courseNames}`;
        });
    }
});
