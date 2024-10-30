document.getElementById('btn_send').addEventListener("click", sendMessage)

function sendMessage () {
    let apiEndpoint = 'http://10.11.7.98:5000/messages'

    if (!validateForm()) {
        alert("Fill the form.")
        return
    }

    let data = {
        "name": document.getElementById('name').value,
        "room": document.getElementById('room').value,
        "house": document.getElementById('house').value,
        "help": document.getElementById('help_description').value ?? '',
        "appointment_situation": document.getElementById('appointment_situation').value
    }

    try {
        cleanInputs()
        fetch(apiEndpoint, {
            method: 'POST', 
            headers: {
              'Content-Type': 'application/json', 
            },
            body: JSON.stringify(data) 
        });
        alert("The staff are being notified, get better!")
    } catch (error) {
        console.log(error)
    }
}

function validateForm() {
    const fields = [
        document.getElementById('name').value.trim(),
        document.getElementById('room').value.trim(),
        document.getElementById('house').value.trim(),
        document.getElementById('appointment_situation').value.trim()
    ]

    return fields.every(field => field !== '')
}

function cleanInputs() {
    document.getElementById('name').value = ""
    document.getElementById('room').value = ""
    document.getElementById('house').value = ""
    document.getElementById('help_description').value = ""
}

