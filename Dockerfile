# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies required for Poetry
RUN apt-get update && apt-get install -y \
    curl \
    libpq-dev \
    gcc \
    && apt-get clean

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy the Poetry files to the container
COPY pyproject.toml poetry.lock* ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

# Copy the rest of the application code
COPY . .

# Set the AIRFLOW_HOME environment variable
ENV AIRFLOW_HOME=/app/airflow

# Expose the port for Airflow webserver
EXPOSE 8080

# We'll set the command in docker-compose.yml

