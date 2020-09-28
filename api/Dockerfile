FROM python:3.6.6-alpine3.7

LABEL maintainer="Eduardo Medeiros Pereira - edu.medeirospereira@gmail.com"
LABEL description="Dockerfile for Python 3 applications with Poetry"

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev
RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

RUN apk del .build-deps gcc musl-dev libffi-dev openssl-dev

EXPOSE 5000

CMD ["python","api.py"]