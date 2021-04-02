FROM python:3.8-alpine3.12

ENV PATH="/scripts:${PATH}"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add postgresql-dev jpeg-dev zlib-dev tree
RUN pip3 install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY . /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN mkdir -p app/vol/web/media

COPY /media /app/vol/web/media/
COPY /media /vol/web/media/


RUN adduser -D user

RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user


CMD ["entrypoint.sh"]

