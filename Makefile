MANAGE := poetry run python3 manage.py

install:
		poetry install

migrate:
		${MANAGE} makemigrations
		${MANAGE} migrate

lint:
		poetry run flake8 --exclude=migrations,admin.py,settings.py\
		task_manager

test:
		poetry run python3 manage.py test ./task_manager/tests

test-coverage:
		poetry run coverage run --source='.' manage.py test ./task_manager/tests
		poetry run coverage xml

dev:
		${MANAGE} runserver

start:
		poetry run gunicorn task_manager.wsgi