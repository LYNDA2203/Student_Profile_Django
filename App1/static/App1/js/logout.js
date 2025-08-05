document.addEventListener('DOMContentLoaded', () => {
    const message = document.querySelector('h2');
    if (message) {
        message.style.opacity = 0;
        message.style.transition = 'opacity 1s ease';

        setTimeout(() => {
            message.style.opacity = 1;
        }, 300); // Fade in effect
    }
});
