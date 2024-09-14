init-container:
	@docker container run -it --rm --name app -v $$(pwd):/app -w /app python:3.12.5-alpine3.20 ash

gen-reqs:
	@pip freeze > ./requirements.txt

server:
	@python manage.py runserver 0.0.0.0:5784
	
migrate:
	@python manage.py migrate

test:
	@pytest tests

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