from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def starting():
    return jsonify({
        "Hi" : "I am Aniket, Testing API's here :)"
    })

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify({"text": "Hello Aniket"})

@app.route('/bye', methods=["GET"])
def bye():
    return jsonify({"bye": "Bye Aniket"})

if __name__ == '__main__':
    app.run(debug=True)
