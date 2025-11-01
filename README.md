Smart Portfolio Site
====================

This is a starter Django project for your dynamic portfolio (Smart Portfolio site).

Quick start (local):
1. Create a virtualenv and activate it.
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver
6. Visit http://127.0.0.1:8000/

To add your intro video:
- Put an MP4 file at projects/static/media/intro.mp4
- Modify landing.html if you want different behavior (autoplay, loop, etc.)

Deploy (Render):
- Push this repo to GitHub and connect to Render.
- Set environment variables (SECRET_KEY, DATABASE_URL) on Render.
