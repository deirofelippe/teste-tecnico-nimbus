FROM python:3.12.5-slim-bookworm

WORKDIR /app/aplicacao-1

ENV PYTHONUNBUFFERED=1 

RUN apt update \
    && apt install -y \
        make curl git \
        # dependências do mysqlclient
        default-libmysqlclient-dev build-essential pkg-config \
    # usuário para ser usado pelo devcontainer
    && adduser -u 1000 --disabled-password --gecos "" py \
    && chown py:py /app/aplicacao-1

COPY --chown=py:py ./requirements.txt ./

RUN pip install -r requirements.txt

COPY --chown=py:py ./ ./

USER py

CMD ["/bin/bash", "/app/aplicacao-1/config-app1-container.sh"]