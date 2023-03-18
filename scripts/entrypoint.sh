#!/bin/sh

set -e

python manage.py collectstatic --noinput

python manage.py migrate

uwsgi --socket :8008 --master --enable-threads --module Eco_Food_game.wsgi