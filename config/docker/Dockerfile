FROM python:3.11.0rc2-slim

ARG WORKING_DIR=/app

ENV PYTHONBUFFERD=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && \
            apt-get install -y --no-install-recommends \
            build-essential \
            libpq-dev \
            && rm -rf /var/lib/apt/lists/*

WORKDIR ${WORKING_DIR}

COPY pyproject.toml poetry.lock ${WORKING_DIR}

RUN python -m pip install --no-cache-dir --upgrade pip && \
          pip install poetry && \
          poetry config virtualenvs.create false && \
          poetry install && \
          rm pyproject.toml poetry.lock

COPY . ${WORKING_DIR}

COPY entrypoint.sh ${WORKING_DIR}/entrypoint.sh

RUN chmod +x ${WORKING_DIR}/entrypoint.sh

ENTRYPOINT ["bash", "entrypoint.sh"]