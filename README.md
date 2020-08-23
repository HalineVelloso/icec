# ICEC

Projeto de controle de estoque feito em Django

# Instalação

Exucutar o install.sh

```
./install.sh
```

Ou 

```
pip3 install django whitenoise gunicorn django-bootstrap4 django-stdimage django-adminlte2 django-filter
sudo apt install gunicorn
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

# Execução

```
python3 manage.py runserver
```

Ou

```
gunicorn Icec.wsgi
```


-Erro 123 (Sintaxe): Pip install django-bootstrap4 django-stdimage
