FROM python:3.12.5-slim-bookworm

WORKDIR /app

RUN apt update \
    && apt install -y \
        make curl \
        # dependências do mysqlclient
        default-libmysqlclient-dev build-essential pkg-config

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

USER 1000:1000

CMD ["/bin/sleep", "inf"]