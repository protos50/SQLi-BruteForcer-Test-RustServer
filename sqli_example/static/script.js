document.getElementById('login-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    const responseDiv = document.getElementById('response');
    responseDiv.innerHTML = ''; // Clear previous response

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'username': username,
                'password': password
            })
        });

        if (response.ok) {
            const responseBody = await response.text();
            responseDiv.innerHTML = `<p style="color: green;">${responseBody}</p>`;
        } else {
            const responseBody = await response.text();
            responseDiv.innerHTML = `<p style="color: red;">${responseBody}</p>`;
        }
    } catch (error) {
        responseDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    }
});
