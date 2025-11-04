# Deploying MetArticles for Free (Fly.io)

This app is ready to deploy on Fly.io's free tier with persistent storage for your SQLite DB and uploads.

## 1) Prerequisites
- Install Fly CLI: https://fly.io/docs/hands-on/install-flyctl/
- Sign up and login: `fly auth signup` then `fly auth login`
- From the project directory (`MetArticles`), run the commands below.

## 2) Initialize app
```bash
fly launch --no-deploy --copy-config
```
- If asked for a name, keep or change `met-articles`.
- When asked to create a Postgres DB, choose No (we use SQLite on a volume).

## 3) Create a volume for data (DB + uploads)
```bash
fly volumes create metarticles_data --region iad --size 1
```
- Region can be changed (e.g., `ams`, `sin`).

## 4) Set secrets
```bash
fly secrets set SESSION_SECRET="your-strong-secret"
```

## 5) Deploy
```bash
fly deploy
```

## 6) Open the app
```bash
fly open
```

Notes:
- The app listens on port 8080 via Gunicorn (set in `Dockerfile`).
- Persistent data is stored at `/data` (configured in `app.py`).
- To scale to 0 (sleep) on inactivity, use Fly autoscaling policies.

---

## Alternative: PythonAnywhere (free, simpler but limited)
- Create a free account at https://www.pythonanywhere.com/
- Upload the project (without Docker) and set a Flask app using `main:app` as the WSGI entry point.
- Use the local SQLite DB; uploads persist in your account storage.
- Free tier has resource and internet access limits.


