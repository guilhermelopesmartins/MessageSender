# Message Sender

At Cumorah Academy, it’s common to have issues when students are sick or need to explain their absences. This project makes things easier by using a form that, once submitted, automatically sends personalized WhatsApp messages to everyone who needs to know.

## Prerequisites

Before starting, make sure you have the following installed on your machine:

- **Python 3.7+**  
- **Git** (optional, to clone the repository)  

Ensure `pip` is up to date:  
```bash
pip install --upgrade pip
```

## Step-by-Step Guide to Run the Application

### 1. Clone the Repository

Clone the repository with the following command:  

```bash
https://github.com/guilhermelopesmartins/MessageSender.git
cd MessageSender
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment to manage the project's dependencies:  

On **Linux/macOS**:  
```bash
python3 -m venv venv
source venv/bin/activate
```

On **Windows**:  
```bash
python -m venv venv
venv\Scripts\activate
```

> **Note:** Once activated, you should see `(venv)` at the beginning of your terminal prompt.

### 3. Install Required Dependencies

With the virtual environment activated, install Flask and `pywhatkit`:  

```bash
pip install Flask pywhatkit
```

> **Note:** These are the only packages required to run the project.

### 4. Add a text file with the contacts

Create a file named `contacts.txt` in the root of the project directory.
Add the phone numbers (including the country code) of the people who should receive messages. Each number should be on a new line.

Example contacts.txt:
```diff
+1234567890
+0987654321
+1123456789
```

### 5. Run the Application

Start the application using the following command:  

```bash
python3 Application.py
```

> **Note:** The application will be available on your local network at port `5000`.

## Contributing

If you want to contribute, please follow the instructions to create a **pull request** or open an **issue** on the repository.

---
