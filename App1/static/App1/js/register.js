
    document.addEventListener('DOMContentLoaded', function() {
        const form = document.querySelector('form');

        form.addEventListener('submit', function(event) {
            // Get form field values
            const emailInput = document.querySelector('input[name="email"]');
            const password1Input = document.querySelector('input[name="password1"]');
            const password2Input = document.querySelector('input[name="password2"]');

            const email = emailInput ? emailInput.value : '';
            const password1 = password1Input ? password1Input.value : '';
            const password2 = password2Input ? password2Input.value : '';

            // Validation checks
            if (email && !email.includes('@')) {
                alert('Please enter a valid email address.');
                event.preventDefault(); // Stop form submission
            } else if (password1 !== password2) {
                alert('Passwords do not match!');
                event.preventDefault();
            }
        });
    });

