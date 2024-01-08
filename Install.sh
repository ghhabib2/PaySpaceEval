#!/bin/bash
echo -ne "\033[0;31m \t Installing the app \n \033[0m"
docker-compose build
echo -ne "\033[0;31m \t Start Calling 'makemigrations' \n \033[0m"
docker-compose run app python manage.py makemigrations
echo -ne "\033[0;31m \t End Calling 'makemigrations' \n \033[0m"

echo -ne "\033[0;31m \t End installing the app \n \033[0m"