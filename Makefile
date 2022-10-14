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

test-coverage:
	poetry run coverage run ./manage.py test
	poetry run coverage html
	poetry run coverage report	

test-coverage-xml:
	poetry run coverage xml

update:
	poetry update

install:
	poetry install
