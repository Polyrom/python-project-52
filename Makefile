start:
	poetry run python manage.py runserver

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

lint:
	poetry run flake8 task_manager

test:
	poetry run ./manage.py test

update:
	poetry update

install:
	poetry install
