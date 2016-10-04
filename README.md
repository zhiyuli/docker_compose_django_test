# docker_compose_django_test

This repo was implemented following the tutorial "Quickstart: Docker Compose and Django"
at https://docs.docker.com/compose/django/
A PDF snapshot is included as Quickstart_ Compose and Django.pdf

Some changes:
1) remove "ADD . /code/" from the last line of Dockerfile
2) change "ports" in docker-compose.yml to "8001:8000"
3) add a very simple django app "my_first_app" that returns a json response at /my_first_app/

How to run:
1) docker-compose run web python manage.py migrate
2) docker up
3) http://127.0.0.1:8001/my_first_app/


