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
2) docker-compose up
3) http://127.0.0.1:8001/my_first_app/

Notes:
1) "myweb" may start accessing "mydb' before "mydb" gets fully started. So may need to re-try migrate,
    or go inside container to migrate
    docker exec -it myweb_container bash
    python manage.py migrate

2) "docker-compose up" creates a network called <FOLDERNAME>_default ('composetest_default' in this case),
    and put all containers into that network.
    docker network ls
    docker network inspect composetest_default

3) "myweb" and "mydb" in docker-compose.yml are service names; "myweb_container" and "mydb_container"
   are container names. Both service name and container name will be resolved to corresponding container
   ip automatically within above network.
   docker exec -it myweb_container bash
   ip address
   ping myweb
   ping myweb_container
   ping mydb
   ping mydb_container

   docker-compose DOES NOT create Environment Variables or change /etc/hosts file to establish networking
   among containers as Legacy container links does in bridge network.

   see "Networking in Compose":
     https://docs.docker.com/compose/networking/
   see "Legacy container links":
     https://docs.docker.com/engine/userguide/networking/default_network/dockerlinks/
   see "Linking containers in user-defined networks":
     https://docs.docker.com/engine/userguide/networking/work-with-networks/#linking-containers-in-user-defined-networks

   cat /etc/hosts

