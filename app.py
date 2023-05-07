from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, welcome to DevOps Zero to Hero batch 3'

@app.route('/health')
def health():
    return 'Server is UP and Running'
