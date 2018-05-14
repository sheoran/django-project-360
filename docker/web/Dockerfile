FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN apt-get update &&\
    apt-get install -y postgresql-client zip tree &&\
    pip install --upgrade pip &&\
    pip install pipenv

RUN mkdir -p /src/
WORKDIR /src/

ADD Pipfile .
ADD Pipfile.lock .
RUN pipenv install --system --deploy

ADD bin bin
ADD manage.py .
ADD yourNameSpace yourNameSpace
