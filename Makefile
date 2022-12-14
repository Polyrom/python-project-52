start:
	poetry run python manage.py runserver

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

railway-migrate:
	poetry run railway run python manage.py migrate

lint:
	poetry run flake8 task_manager labels users tasks statuses

test:
	poetry run ./manage.py test

test-coverage:
	poetry run coverage run ./manage.py test
	poetry run coverage xml
	poetry run coverage report

update:
	poetry update

install:
	poetry install

secretkey:
	poetry run python -c 'from django.utils.crypto import get_random_string; print(get_random_string(40))'
