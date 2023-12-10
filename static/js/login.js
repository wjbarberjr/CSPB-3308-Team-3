document.addEventListener('DOMContentLoaded', function () {
    // Function to handle form submission
    function handleFormSubmit(event) {
        console.log('Form submitted');
        // Prevent the default form submission behavior
        event.preventDefault();

        // Collect form data
        const formData = new FormData(event.target);

        fetch('/login', {
            method: 'POST',
            body: formData,
            credentials: 'include'
        })
        .then(response => {
            if (!response.ok) {
                console.error('Server Error:', response.statusText);
                throw new Error(`Server responded with ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            console.log('Server Response:', data);

            // You can handle the server response here (e.g., redirect or show a message)
        })
        .catch(error => console.error('Error:', error));
    }

    // Use window.onload to ensure the script runs after the DOM is fully loaded
    window.onload = function() {
        // Find the login form by its ID
        const loginForm = document.getElementById('loginForm');

        // Attach the form submission handler
        loginForm.addEventListener('submit', handleFormSubmit);
    };
});
