FROM python:3.12.2-slim-bookworm AS builder

ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_OPTIONS_ALWAYS_COPY=true

RUN pip install poetry==1.7.1
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.options.always-copy true
RUN poetry install

FROM python:3.12.2-slim-bookworm
WORKDIR /usr/local/app

COPY --from=builder /.venv /.venv
ENV PATH="/.venv/bin:$PATH"
COPY implementation_provider.py pyproject.toml ./
COPY ./src/ ./src/
CMD ["fastapi", "run", "implementation_provider.py", "--port", "8000"]

EXPOSE 8000
