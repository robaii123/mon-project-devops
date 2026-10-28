# 🚀 Pipeline CI/CD Complet : API Python (Flask) + Redis + Docker + GitHub Actions

![CI/CD Pipeline](https://github.com/robaii123/mon-project-devops/actions/workflows/pipeline.yml/badge.svg)

Ce projet démontre la mise en place d'une architecture **DevOps complète de bout en bout (CI/CD)**. L'application est une API REST en Python (Flask) connectée à une base de données **Redis**, entièrement conteneurisée avec **Docker** et déployée automatiquement sur le Cloud (**Render**) à chaque `git push` via **GitHub Actions**.

🔗 **Démo en direct (Live API) :** [https://mon-api-devops.onrender.com](https://mon-api-devops.onrender.com)

---

## 🏗️ Architecture du Pipeline CI/CD

À chaque modification envoyée sur la branche `main`, le workflow GitHub Actions exécute automatiquement 3 étapes :

```text
[Code Push (GitHub)] 
       │
       ▼
1. 🧪 Job: run-tests (CI) ──────> Exécute les tests unitaires avec Pytest
       │
       ▼
2. 🐳 Job: build-and-push (CI) ─> Construit l'image Docker et la publie sur Docker Hub
       │
       ▼
3. ☁️ Job: deploy (CD) ─────────> Déclenche le Webhook Render pour mettre à jour la production
```

---

## 🛠️ Technologies Utilisées

* **Backend :** Python 3.12, Flask
* **Base de données :** Redis 7 (Compteur de visites en temps réel)
* **Tests :** Pytest
* **Conteneurisation :** Docker (`Dockerfile` optimisé par cache de layers), Docker Compose (`docker-compose.yml`)
* **CI/CD :** GitHub Actions, Docker Hub
* **Cloud Hosting :** Render (Web Service + Redis Key-Value)

---

## 💻 Lancer le projet en local (avec Docker Compose)

Vous n'avez même pas besoin d'installer Python ou Redis sur votre machine. Assurez-vous simplement d'avoir **Docker** installé, puis lancez :

```bash
# 1. Cloner le repository
git clone [https://github.com/robaii123/mon-project-devops.git](https://github.com/robaii123/mon-project-devops.git)
cd mon-project-devops

# 2. Construire et démarrer l'API + la base de données Redis en arrière-plan
docker compose up -d --build
```

L'API sera immédiatement accessible sur : **`http://localhost:8080`**

Pour arrêter les conteneurs proprement :
```bash
docker compose down
```

---

## 📡 Endpoints de l'API

* **`GET /`** : Retourne le statut de l'API, l'environnement actuel et le nombre de visites stocké dans Redis :
  ```json
  {
    "environment": "production",
    "message": "Mon Pipeline CI/CD 100% Automatique fonctionne !",
    "status": "success",
    "visites": 113
  }
  ```
* **`GET /add/<int:a>/<int:b>`** : Additionne deux nombres entiers (ex: `/add/5/3` retourne `{"result": 8}`).

---

## 🧪 Lancer les tests manuellement

```bash
pip install -r requirements.txt
pytest
```