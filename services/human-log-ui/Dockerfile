# Image documentation:
# https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
FROM tiangolo/uwsgi-nginx-flask:python3.7

WORKDIR /app

# Install poetry, using method from:
# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
RUN pip install --upgrade pip
RUN pip install poetry==0.12.17

# Install project dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY ./app /app
