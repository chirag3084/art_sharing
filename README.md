# modern-django-1000px

## how to install this project

1. create your virtualenv (optional)

```bash
$ pip3 install virtualenv
$ virtualenv -python3 venv
$ source ./venv/bin/activate
```

2. install project dependencies

```bash
  (venv) $ pip install -Ur ./requirements/base.txt
```

## how to run the server

1. migrate database (first time only)

```bash
  (venv) $ python manage.py makemigrations
  (venv) $ python manage.py migrate
```

2. run server

* you can specify another settings file, according to your environment.

  ```bash
    (venv) $ export DJANGO_SETTINGS_MODULE="config.settings.local.py"
    (venv) $ python manage.py runserver
  ```
