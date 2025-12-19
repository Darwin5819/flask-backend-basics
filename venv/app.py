from flask import Flask, jsonify
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


if __name__ == "__main__":
    app.run(debug=True)
