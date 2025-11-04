# Deploying MetArticles on PythonAnywhere (Free Plan)

This guide gets your Flask app running on PythonAnywhere without Docker.

## 1) Prepare your code locally
- Ensure these files exist (added already):
  - `requirements.txt`
  - `wsgi_example.py`

## 2) Create a PythonAnywhere account
- Go to `https://www.pythonanywhere.com/` and sign up for a free account.

## 3) Upload code to PythonAnywhere
Option A: Zip upload (simplest)
- Zip the project folder `MetArticles` on your PC.
- On PythonAnywhere, open the Files tab and upload the zip.
- In the Bash console, unzip to `~/MetArticles`.

Option B: Git (recommended if you have a repo)
- In a Bash console on PythonAnywhere:
```bash
cd ~
git clone <your-repo-url> MetArticles
```

## 4) Create a virtualenv and install deps
- Open a Bash console on PythonAnywhere, then:
```bash
cd ~/MetArticles
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## 5) Create a Web app
- Go to the Web tab → Add a new web app → Manual configuration → Python 3.10 (or closest).
- Set the Working directory to: `/home/<your_username>/MetArticles`
- WSGI file: click to edit, and replace its contents with:
```python
import os, sys
project_home = os.path.expanduser('~/MetArticles')
if project_home not in sys.path:
    sys.path.insert(0, project_home)
from main import app as application
```

## 6) Configure virtualenv
- On the Web tab, set Virtualenv to: `/home/<your_username>/MetArticles/venv`

## 7) Environment and static files
- In the Web tab → Environment variables, add:
  - `SESSION_SECRET` = a strong random string
- Static files: add a mapping:
  - URL: `/static/` → Directory: `/home/<your_username>/MetArticles/static`

## 8) Reload and test
- Click Reload on the Web tab.
- Open your app (the link is shown at the top of the Web tab).

Notes
- SQLite DB `app.db` will be created in `/home/<your_username>/MetArticles` automatically on first run.
- Uploaded PDFs will be stored in `uploads/` in the project folder.
- If you get import errors, confirm the venv path and WSGI contents.
- View server error logs on the Web tab (error log and server log).


