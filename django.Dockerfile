# Base Image
FROM python:3.11.3-alpine3.18

LABEL org.opencontainers.image.authors="ghhabib2@gmail.com"
LABEL version="0.1"

ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

COPY requirements /requirements
COPY ./scripts /scripts
COPY ./src /src

WORKDIR src

# port where the Django app runs
EXPOSE 80


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip
RUN apk add --update --no-cache postgresql-client
RUN apk add --update  postgresql-client build-base postgresql-dev musl-dev linux-headers libffi-dev libxslt-dev libxml2-dev
RUN    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers libffi-dev libjpeg zlib-dev jpeg-dev gcc musl-dev libxslt libxml2

RUN /py/bin/pip install -r /requirements/development.txt

RUN chmod -R +x /scripts && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    adduser --disabled-password --no-create-home mnapp_user && \
    chown -R mnapp_user:mnapp_user /vol && \
    chmod -R 755 /vol

ENV PATH="/scripts:/py/bin:$PATH"

USER mnapp_user

CMD ["run.sh"]