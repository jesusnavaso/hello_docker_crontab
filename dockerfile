FROM python:3.9-slim

RUN apt update
RUN apt install -y git
RUN apt install -y cron
RUN git clone "https://github.com/jesusnavaso/hello_docker_crontab.git" /hello_docker_crontab
RUN cd /hello_docker_crontab && crontab crontab

CMD cron
