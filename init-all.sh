#!/bin/bash

echo "==========> Iniciando o docker"
docker compose up -d --build

echo "==========> Healthcheck do danco de dados"
while true; do
    sleep 3
    docker compose exec -it db bash -c "mysqladmin -u root -proot ping -h localhost" | grep "mysqld is alive"
    if [ $? -eq 0 ]; then
        break;
    fi
done

echo "==========> Executando migrations"
docker compose exec -it app1 bash -c "make py-mig"

echo "==========> Gerando cobertura de código"
docker compose exec -it app1 bash -c "make test-cov"

echo "==========> Iniciando o servidor"
docker compose exec -it app1 bash -c "make py-server"