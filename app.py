from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    env_name = os.getenv("APP_ENV", "developpement")
    return jsonify({
        "message": "Mon API Docker + GitHub Actions fonctionne !",
        "environment": env_name,
        "status": "success"
    })

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

if __name__ == "__main__":
    # host="0.0.0.0" est OBLIGATOIRE avec Docker pour accepter les connexions extérieures !
    app.run(host="0.0.0.0", port=5000)