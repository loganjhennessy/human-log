FROM python:3.7-alpine

WORKDIR /app

# Setup alpine for building python packages
RUN apk add build-base libffi-dev openssl-dev

# Lets print statements come out when running behind gunicorn
ENV PYTHONUNBUFFERED=1

# Install poetry, using method from:
# https://stackoverflow.com/questions/53835198/integrating-python-poetry-with-docker
RUN pip install --upgrade pip
RUN pip install poetry==0.12.17

# Install project dependencies
COPY poetry.lock pyproject.toml /app/
RUN poetry config settings.virtualenvs.create false
RUN poetry install

COPY ./app /app

CMD gunicorn main:app -b 0.0.0.0:$PORT -w 4