from flask import Flask, jsonify, request

from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API running"})

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

@app.route("/hello/<name>")
def hello(name):
    return jsonify({"greeting": f"Hello {name}!"})


@app.route("/info")
def info():
    return jsonify({
        "app": "Flask Learning API",
        "developer": "Darwin",
        "date": str(date.today())
    }), 200

@app.route("/welcome", methods=["POST"])
def welcome():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify({"message": f"Welcome, {name}!"}), 200

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)

    return jsonify({"result": a + b}), 200


if __name__ == "__main__":
    app.run(debug=True)
