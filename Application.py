from flask import Flask, jsonify, request , render_template
from flask_cors import CORS
import MessageDeliver
from threading import Lock

app = Flask(__name__)
CORS(app)

request_lock = Lock()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/messages', methods=['POST'])
def send_message():
    with request_lock:
        content = request.get_json()
        return MessageDeliver.send_messages(content)

app.run(host="0.0.0.0", port=5000, debug=True)