FROM python:3.10-buster as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
# RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN pip3 install pipenv
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --deploy

COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

COPY . .
# ENTRYPOINT ["python", "-m", "http.server"]
CMD ["python"]