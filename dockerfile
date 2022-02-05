FROM python:3.9-slim

COPY . /hello_docker_crontab

RUN apt update
RUN apt install -y git
RUN apt install -y cron
RUN cd /hello_docker_crontab && crontab crontab

CMD ["/bin/bash", "-c", "cron"]
