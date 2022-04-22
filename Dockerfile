FROM python:3.10-buster as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
EXPOSE 5000
# RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN pip3 install pipenv
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PMP_MICROSERVICE_CONFIG /home/appuser/.env.docker

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

RUN useradd -ms /bin/bash appuser
WORKDIR /home/appuser
USER appuser

COPY . .
ENV PYTHONPATH=.
ENTRYPOINT FLASK_APP=/home/appuser/services/service.py flask run --host=0.0.0.0
# CMD ["python"]