web: gunicorn viz_server.wsgi

makemigrations: python manage.py makemigrations
applychanges: python3 manage.py migrate
start: python manage.py runserver
