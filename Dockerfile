FROM python:3.12.5-slim-bookworm

WORKDIR /app

ENV PYTHONUNBUFFERED=1 

RUN apt update \
    && apt install -y \
        make curl git \
        # dependências do mysqlclient
        default-libmysqlclient-dev build-essential pkg-config \
    # usuário para ser usado pelo devcontainer
    && adduser -u 5678 --disabled-password --gecos "" py

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

USER py

CMD ["/bin/sleep", "inf"]