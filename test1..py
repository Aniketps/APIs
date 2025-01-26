from flask import flask, jsonify, requests

app = Flask(__name__)

@app.route('/greet', method=['GET'])
def greet():
   return jsonify({"text": "HEllo Aniket"})

@app.route('/bye', method=["GET"])
def bye():
    return jsonify({"bye" : "Bye Aniket"})

if __name__ == '__main__':
    app.run(debug=true)