start:
	poetry run python manage.py runserver

lint:
	poetry run flake8 task_manager

update:
	poetry update

install:
	poetry install
