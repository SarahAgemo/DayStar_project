
        document.addEventListener('DOMContentLoaded', function () {
            const form = document.getElementById('add-baby-form');
            const nameInput = document.getElementById('baby-name');
            // Add similar variables for other form inputs

            form.addEventListener('submit', function (event) {
                event.preventDefault(); // Prevent form submission

                // Validate form fields
                let isValid = true;
                const errors = {};

                if (nameInput.value.trim() === '') {
                    isValid = false;
                    errors['baby_name'] = 'Please enter baby name.';
                }
                // Add similar validations for other fields

                // Display error messages
                const messageContainer = document.getElementById('message-container');
                messageContainer.innerHTML = ''; // Clear previous messages

                if (!isValid) {
                    Object.keys(errors).forEach(field => {
                        const errorDiv = document.createElement('div');
                        errorDiv.textContent = errors[field];
                        messageContainer.appendChild(errorDiv);
                    });
                } else {
                    // Form is valid, submit the form
                    form.submit();
                }
            });
        });
    