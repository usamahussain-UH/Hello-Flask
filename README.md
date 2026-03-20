# Hello-Flask

This project is a Flask-based travel showcase website with search, slider, country details and modern UI.

## Deployment package for GitHub + Render/Fly/PythonAnywhere

### Files included
- `app.py` - main Flask application
- `requirements.txt` - dependencies for Python environment
- `Procfile` - web process command (for Heroku/Render)
- `runtime.txt` - Python version for Heroku
- `README.md` - project overview and deployment instructions

### Install and run locally
1. `git clone <repo-url>`
2. `cd Hello-Flask`
3. Create venv: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux)
4. `pip install -r requirements.txt`
5. `python app.py` (or `gunicorn app:app` for production)
6. Open in browser: `http://localhost:5000`

### Deploy on Render (quickest)
1. Push to GitHub:
   - `git add .`
   - `git commit -m "Deploy package"`
   - `git push`
2. Go to Render.com > New Web Service > Connect your GitHub repository
3. Set environment:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. Deploy and open public URL.

### Deploy on Fly.io
1. `fly launch` (choose app name + region)
2. Set `app.py` server command in `fly.toml`: `gunicorn app:app --bind 0.0.0.0:8080`
3. `fly deploy`

### Deploy on PythonAnywhere
1. Create web app (Flask)
2. Upload files and set WSGI to `app.py`
3. Reload web app

### Deploy on Heroku
1. `heroku create`
2. `git push heroku main`
3. `heroku open`

## Notes
- The app includes backend endpoints (`/`, `/search`, `/country/<country>`) so static-only hosts will not support full functionality.
- For a static-only version, export HTML/CSS manually.

