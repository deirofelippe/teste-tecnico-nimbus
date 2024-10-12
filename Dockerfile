FROM python:3.12.5-slim-bookworm

WORKDIR /app

ENV PYTHONUNBUFFERED=1 

RUN apt update \
    && apt install -y \
        make curl wget git netcat-openbsd mtr \
        # dependências do mysqlclient
        default-libmysqlclient-dev build-essential pkg-config \
    # usuário para ser usado pelo devcontainer
    && adduser -u 1000 --disabled-password --gecos "" py \
    && cd /tmp \
    # instala o kubernetes
    && wget "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl \
    # configura o owner do /app
    && cd /app \
    && chown py:py /app 

COPY --chown=py:py ./ ./

USER py

CMD ["/bin/bash", "/app/config-develop-container.sh"]
