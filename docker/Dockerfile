# ---------------------------------------------------------------------------------------
# Base
# ---------------------------------------------------------------------------------------

FROM python:3.11-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && \
    apt-get install --no-install-recommends -y \
    # deps for internationalization and localization
    gettext \
    # deps for multimedia files and streams
    ffmpeg \
    # deps for psycopg2
    libpq-dev \
    python3-dev \
    gcc

# ---------------------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------------------

FROM base as builder

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Install Poetry
RUN pip install poetry==1.8.2

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --no-root # --without-dev

# ---------------------------------------------------------------------------------------
# Runtime
# ---------------------------------------------------------------------------------------

FROM base as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY src .
