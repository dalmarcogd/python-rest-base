FROM python:buster

RUN pip install -U pip pipenv

WORKDIR app

ADD Pipfile* ./

RUN pipenv install --system

ADD . .

ENTRYPOINT uvicorn src.app:app --workers 4