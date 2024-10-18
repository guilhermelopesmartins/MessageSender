from flask import Flask, jsonify, request 
import MessageDeliver

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'API WORKING'

@app.route('/messages', methods=['POST'])
def send_message():
    content = request.get_json()
    return MessageDeliver.send_messages(content)

app.run(port=5000, host='localhost', debug=True)