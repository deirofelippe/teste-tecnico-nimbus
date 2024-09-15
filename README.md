# Teste Técnico da NIMBUS

## Sumário

- [Tecnologias e libs usadas](#tecnologias-e-ferramentas-usadas)
- [Como executar?](#como-executar)
    - [Como executar?](#iniciar-tudo)
    - [Iniciar o servidor](#iniciar-o-servidor)
    - [Como executar os testes?](#como-executar-os-testes)
    - [Gerar o relatório de cobertura de código?](#gerar-o-relatório-de-cobertura-de-código)
- [Arquitetura usada e desenho](#arquitetura-usada-e-desenho)
- [Padrões usados](#padrões-usados)
- [Client HTTP](#client-http-testar-endpoints)
- [GUI para banco de dados](#gui-para-banco-de-dados)
- [Checklist](#checklist)
- [Melhoria no sistema](#melhoria-no-sistema)

## Tecnologias e ferramentas usadas

- Python 3.12.5
- Django e Django REST framework
- PyTest, Faker, PyTest Mock, PyTest Django
- Docker 20.10.23
- Docker Compose 2.15.1
- Dev Container
- MySQL e phpMyAdmin
- Cerberus
- Loguru
- ReportLab
- CronTab

## Como executar?

### Iniciar tudo

- `make init-all`: inicia os containers, executa as migrations, gera a cobertura de código e inicia o servidor.

**OU**

- `make up`: inicia os containers.
- `make start-server`: executa as migrations e inicia o servidor.

**OU**

- `docker compose up -d`: inicia os containers.
- `docker compose exec -it app bash`: acessa o container.
    - `python manage.py migrate`: executa as migrations.
    - `python manage.py runserver 0.0.0.0:5784`: inicia o servidor.

### Iniciar o servidor

- `make start-server`

### Como executar os testes?

- `make exec`: acessa o container.
- `make test`: executa os testes.

### Gerar o relatório de cobertura de código?

- `make exec-root`: acessa o container como root.
- `make test-cov`: executa a geração do relatório de cobertura de código.

## Arquitetura usada e desenho

Por quê foi usada arquitetura em camadas?

- Facilita o mock para os testes de integração e de unidade.
- Separa as responsabilidades do código, facilitando a manutenção.

### Desenho da arquitetura

- Service: orquestra a lógica de negócio.
- Repository: meio para qualquer acesso a serviços externos como api, banco de dados e etc.

![](./docs/arquitetura.png)

## Padrões usados

- Service
- Repository
- Fail Fast/Early Return
- Dependency Injection
- Single Responsability Principle (SRP)

## Client HTTP (Testar endpoints)

Foi usado a extensão Rest Client do VSCode para os testar os endpoints (como insomnia ou postman).

![](./docs/images/rest-client.png)

## GUI para banco de dados

Foi usado o phpMyAdmin como interface gráfica para o banco de dados.

![](./docs/images/php-my-admin.png)

## Checklist

- Aplicação 1
    - [x] API com Django
    - [x] Logs com loguru
    - [x] Testes automatizados com PyTest
    - [ ] Testar todas as possibilidades de input, erros e branches
    - [x] Banco com MySQL
    - [x] API Versioning
    - [x] Tratamento de error
    - [x] Validações
    - [x] Separação por layers
    - [x] Commits semânticos

- Aplicação 2

## Aplicação 1

## Melhoria no sistema
