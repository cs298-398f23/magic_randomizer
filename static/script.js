// static/script.js

function updateTextBox() {
    var textBox = document.getElementById("textBox");

    // Make a GET request to the Flask server
    fetch('/update_text')
        .then(response => response.json())
        .then(data => {
            // Update the text box content with the response from the server
            textBox.value = data.message;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
