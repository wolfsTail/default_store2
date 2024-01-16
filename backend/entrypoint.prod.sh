#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Postgres not available, waiting..."

    # Проверяем доступность хоста и порта
    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL on air"
fi

exec "$@"