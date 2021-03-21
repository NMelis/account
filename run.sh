#!/usr/bin/env bash

docker-compose build
docker-compose up -d
echo 'Wait 10 seconds...'
sleep 10
docker-compose logs -f --tail=300 web celery celery-beat
