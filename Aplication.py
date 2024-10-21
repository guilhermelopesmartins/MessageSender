from flask import Flask, jsonify, request 
from flask_cors import CORS
import MessageDeliver

app = Flask(__name__)
CORS(app)

@app.route('/')
def homepage():
    return 'API WORKING'

@app.route('/messages', methods=['POST'])
def send_message():
    content = request.get_json()
    return MessageDeliver.send_messages(content)

app.run(port=5000, host='localhost', debug=True)