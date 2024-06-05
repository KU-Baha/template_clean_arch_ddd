# ---------------------------------------------------------------------------------------
# Base
# ---------------------------------------------------------------------------------------

FROM python:3.11-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.8.1 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# ---------------------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------------------

FROM base as builder

# System deps
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    # deps for installing poetry
    curl \
    # deps for building python deps
    build-essential \
    # deps for internationalization and localization
    gettext \
    # deps for multimedia files and streams
    ffmpeg \
    # deps for psycopg2
    libpq-dev \
    gcc

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=$POETRY_HOME POETRY_VERSION=$POETRY_VERSION python3 -

# copy project requirement files here to ensure they will be cached.
WORKDIR $PYSETUP_PATH

COPY pyproject.toml poetry.lock ./

RUN $POETRY_HOME/bin/poetry install

# ---------------------------------------------------------------------------------------
# Runtime
# ---------------------------------------------------------------------------------------

FROM base as runtime

ENV FASTAPI_ENV=development
WORKDIR $PYSETUP_PATH

# copy in our built poetry + venv
COPY --from=builder $POETRY_HOME $POETRY_HOME
COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH

# quicker install as runtime deps are already installed
RUN poetry install

WORKDIR /app

COPY src .

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY docker/start.sh /start.sh
RUN chmod +x /start.sh

ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000

