FROM python:3.12.5-slim-bookworm

WORKDIR /app/aplicacao-2

ENV PYTHONUNBUFFERED=1 

RUN apt update \
    && apt install -y \
        make curl git fontconfig \
    # usuário para ser usado pelo devcontainer
    && adduser -u 1000 --disabled-password --gecos "" py

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

USER py

CMD ["/bin/sleep", "inf"]