# 📚 TP DevOps : Application Flask + PostgreSQL + Jenkins CI/CD

Ce projet est une application web simple en architecture **2 tiers** développée en **Python (Flask)** avec une base de données **PostgreSQL**.  
Elle permet d’**ajouter** et **supprimer** des étudiants, avec une interface utilisateur intégrée (HTML + CSS).  
L’objectif pédagogique est de mettre en pratique Docker, Docker Compose, et Jenkins CI/CD.

---

## 🧱 Architecture

|-- Flask (backend + frontend intégré)
|-- PostgreSQL (base de données)

Les services sont orchestrés via **Docker Compose** avec un réseau personnalisé `tp-net` et un `healthcheck` pour assurer le bon démarrage de la base de données avant l’application.

---

## 🚀 Démarrage rapide

### 🔧 Prérequis

- Docker & Docker Compose installés
- (Optionnel) Jenkins installé pour la CI/CD

### ▶️ Lancer avec Docker Compose

```bash
docker compose up --build
```
L'application sera disponible sur http://localhost:5000

Structure du projet
bash
Copier
Modifier
.
├── app.py                 # Application Flask
├── index.html             # Frontend HTML + CSS intégré
├── requirements.txt       # Dépendances Python
├── Dockerfile             # Image de l'application
├── docker-compose.yml     # Orchestration des services
├── Jenkinsfile            # Pipeline CI/CD
└── README.md              # Documentation du projet


Pipeline Jenkins (CI/CD)
Un Jenkinsfile est fourni avec 3 étapes :

Clone du dépôt Git

Build des images via docker compose build

Déploiement avec docker compose up -d

⚠️ Jenkins doit avoir accès au Docker daemon de l’agent.


Variables d’environnement utilisées
Définies dans docker-compose.yml :

POSTGRES_USER=user

POSTGRES_PASSWORD=pass

POSTGRES_DB=etudiants
