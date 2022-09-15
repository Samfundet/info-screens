# info-screens

Django application to support info screens at Samfundet.

We recommend installing `pyenv` however you can for your operating system.

## Setup environment variables

```sh
cp .env.example .env
```

- Then fill in missing variables

## Project setup

```sh
python3 -m pip install pipenv
```

```sh
python3 -m pipenv install
```

```sh
python3 -m pipenv run python manage.py makemigrations
```

```sh
python3 -m pipenv run python manage.py migrate
```

```sh
python3 -m pipenv run python manage.py runserver
```

### Other useful commands

```sh
python3 -m pipenv run python manage.py
```

```sh
python3 -m pipenv run python manage.py deletemigrations
```

```sh
python3 -m pipenv run python manage.py cleanstart
```

```sh
python3 -m pipenv run python manage.py collectstatic
```

## Deployment
The project exist at:
```sh
/home/cassarossa/lim/web-intern/projects/info-screens
```
