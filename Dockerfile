FROM python:3.9-alpine

ENV PATH="/scripts:${PATH}"

USER root

COPY ./Eco_Food_game/requirements.txt Eco_Food_game/requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r ./Eco_Food_game/requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./Eco_Food_game /Eco_Food_game

WORKDIR /Eco_Food_game
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir --parents /vol/web/media
RUN mkdir --parents /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
#USER user

CMD ["entrypoint.sh"]