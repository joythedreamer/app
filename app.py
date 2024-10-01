from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Welcome to our API service!"})

@app.route('/status')
def status():
    api_key = os.environ.get('API_KEY')
    return jsonify({
        "status": "operational",
        "api_key_set": bool(api_key)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)