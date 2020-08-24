sudo apt install python3 python3-pip gunicorn
pip3 install django whitenoise gunicorn django-bootstrap4 django-stdimage django-adminlte2 django-filter
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser