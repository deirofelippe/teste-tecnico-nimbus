init-tmp-container:
	@docker container run -it --rm --name app -v $$(pwd):/app -w /app python:3.12.5-alpine3.20 ash

py-reqs:
	@pip freeze > ./requirements.txt

test-debug:
	@python -m pytest -s -v tests/

test:
	@python -m pytest -v tests/
	
## APLICAÇÃO 1

py-server:
	@python manage.py runserver 0.0.0.0:5784
	
py-mig:
	@python manage.py migrate

py-mkmig:
	@python manage.py makemigrations customer

test-cov:
	@python -m coverage run -m pytest tests/
	@python -m coverage html

## DOCKER

ci-cd: 
	@gh extension exec act -j build

init-all: up
finish-all: down

init-all-k8s: 
	@./init-kubernetes.sh

app1-start:
	@docker compose exec -it app1 bash -c "make py-mig ; make py-server"

app2-start:
	@docker compose exec -it app2 bash -c "python main.py"

exec-develop:
	@docker container exec -it develop-nimbus bash

exec-app1:
	@docker compose exec -it app1 bash

exec-app1-root:
	@docker compose exec -u root app1 bash

exec-app2:
	@docker compose exec -it app2 bash

exec-app2-root:
	@docker compose exec -u root app2 bash

up:
	@docker compose up -d --build

down:
	@docker compose down

ps:
	@docker compose ps -a