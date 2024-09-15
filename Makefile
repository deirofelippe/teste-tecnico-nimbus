init-tmp-container:
	@docker container run -it --rm --name app -v $$(pwd):/app -w /app python:3.12.5-alpine3.20 ash

## APLICAÇÃO 1

py-reqs:
	@pip freeze > ./requirements.txt

py-server:
	@python manage.py runserver 0.0.0.0:5784
	
py-mig:
	@python manage.py migrate

py-mkmig:
	@python manage.py makemigrations customer

test-debug:
	@python -m pytest -s -v tests/

test:
	@python -m pytest -v tests/

test-cov:
	@python -m coverage run -m pytest tests/
	@python -m coverage html

## DOCKER

init-all: 
	@/bin/bash ./init-all.sh

start-server:
	@docker compose exec -it app1 bash -c "make py-mig ; make py-server"

exec:
	@docker compose exec -it app1 bash

exec-root:
	@docker compose exec -u root app1 bash

up:
	@docker compose up -d --build

down:
	@docker compose down

ps:
	@docker compose ps -a