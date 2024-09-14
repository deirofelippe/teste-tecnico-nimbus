init-container:
	@docker container run -it --rm --name app -v $$(pwd):/app -w /app python:3.12.5-alpine3.20 ash

gen-reqs:
	@pip freeze > ./requirements.txt

server:
	@python manage.py runserver 0.0.0.0:5784
	
migrate:
	@python manage.py migrate

mkmigrate:
	@python manage.py makemigrations customer

test-debug:
	@python -m pytest -s -v tests/

test:
	@python -m pytest -v tests/

test-cov:
	@python -m coverage run -m pytest tests/
	@python -m coverage html

## DOCKER

exec:
	@docker compose exec -it app bash

exec-root:
	@docker compose exec -u root app bash

up:
	@docker compose up -d --build

down:
	@docker compose down

ps:
	@docker compose ps -a