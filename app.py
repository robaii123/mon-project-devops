from flask import Flask, jsonify
import os
import redis

app = Flask(__name__)

# On récupère le nom du conteneur de la base de données via une variable d'environnement !
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Connexion à la base de données Redis
db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route("/")
def home():
    env_name = os.getenv("APP_ENV", "developpement")
    try:
        # Incrémente le compteur de visites de +1 dans la base de données
        visites = db.incr("compteur_visites")
    except redis.ConnectionError:
        # Si la base de données n'est pas allumée (ex: pendant pytest), on ne plante pas !
        visites = "Base de donnees non connectee"

    return jsonify({
        "message": "Mon API Pro Docker + Redis + GitHub Actions !",
        "environment": env_name,
        "visites": visites,
        "status": "success"
    })

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)