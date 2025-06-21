# 🗂️ Waste Reporting App

## 🌍 Projet : Waste Reporting (Signalement de dépôts sauvages)

Mini-projet académique fullstack (FastAPI + React + MySQL) avec authentification sécurisée et interface de test.

---

## 📦 Technologies utilisées

| Côté      | Technologies                          |
|-----------|----------------------------------------|
| Backend   | FastAPI, SQLAlchemy, JWT, Pydantic     |
| Frontend  | React.js, Axios, TailwindCSS (partiel) |
| BDD       | MySQL 8                                |
| Auth      | JWT (Access Token)                     |
| DevOps    | .env (pas Dockerisé)                   |

---

## ✅ Fonctionnalités terminées

- Authentification sécurisée avec JWT (inscription & connexion)
- Création d’un utilisateur et login via `/register` et `/login`
- CRUD basique sur l’entité `WasteSpot`
- Test de l’API backend via Swagger (`/docs`)
- Frontend de test : Login + appel backend

## ⚠️ Limites

🚧 Le frontend n’est **pas terminé** à cause de plusieurs erreurs rencontrées (erreurs CORS, gestion formulaire, état token).  
👉 Un frontend **basique** a été mis en place uniquement pour tester le backend.

---

## 🧪 Installation locale

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger : http://127.0.0.1:8000/docs

### 2. Frontend (test uniquement)

```bash
cd frontend
npm install
npm run dev
```

Test basique du login uniquement.

---

## 🧱 Structure du projet

```
backend/
  app/
    ├── main.py
    ├── models.py
    ├── schemas.py
    ├── auth.py
    ├── crud.py
    └── database.py

frontend/
  src/
    ├── components/
    │   └── LoginForm.jsx
    ├── pages/
    │   ├── LoginPage.jsx
    │   └── BookListPage.jsx
    ├── App.jsx
    ├── index.js
    └── services/
        └── api.js
```

---

## 🔐 Routes testées

### POST /register

```json
{
  "email": "test@example.com",
  "password": "lebonmdp"
}
```

### POST /login

Content-Type: `application/x-www-form-urlencoded`

```
grant_type=password
username=test@example.com
password=lebonmdp
```

---

## 📌 .env (exemple backend)

```
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/waste_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## ✍️ Auteur

Projet réalisé par Oubay aazibou(back-end) et reda ifrah (ci/cd) et ilyass boukaya (frontend)  dans le cadre d’un rendu académique.  
Date de livraison : 21/06/2025
(la partie front-end va etre refaite et terminer)