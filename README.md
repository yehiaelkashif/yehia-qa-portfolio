# Yehia Salah — FinTech QA Portfolio

Django portfolio website for Yehia Salah, focused on FinTech QA, API testing, test automation, Playwright, Appium, POS testing and UAT.

## Run locally

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Deploy on Render

This repository includes `render.yaml`, `build.sh`, Gunicorn and WhiteNoise configuration.

1. Push the project to a GitHub repository.
2. Sign in to Render and create a Blueprint (or a Web Service) from the repository.
3. Render reads `render.yaml` and builds the Django app.
4. After deployment, Render provides an `onrender.com` URL.

If creating the Web Service manually:
- Build command: `bash build.sh`
- Start command: `gunicorn config.wsgi:application`
- Environment variable: `DEBUG=False`
- Environment variable: `SECRET_KEY=<generate a strong random value>`

The site does not rely on persistent application data. SQLite is only used for Django's default framework database and is not used to store portfolio content.
