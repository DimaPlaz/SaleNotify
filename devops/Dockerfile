FROM python:3.11

COPY pyproject.toml /pyproject.toml
RUN pip install -U pip poetry
RUN poetry config virtualenvs.create false && poetry install

COPY src /src
COPY migrations /migrations

WORKDIR /src
ENV PYTHONPATH=/src
