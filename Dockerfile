# Use a full Python base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Install system dependencies required for Poetry and Spark
RUN apt-get update && apt-get install -y \
    curl \
    libpq-dev \
    gcc \
    openjdk-17-jdk \
    && apt-get clean

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy the Poetry files to the container
COPY pyproject.toml poetry.lock* ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

# Install Spark
RUN curl -sSL https://archive.apache.org/dist/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz | tar -xz -C /opt/ && \
    ln -s /opt/spark-3.4.0-bin-hadoop3 /opt/spark

# Set JAVA_HOME environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64  
ENV PATH="$JAVA_HOME/bin:$PATH:/opt/spark/bin"

# Copy the rest of the application code
COPY . .

# Set the AIRFLOW_HOME environment variable
ENV AIRFLOW_HOME=/app/airflow

# Expose the port for Airflow webserver
EXPOSE 8080

# We'll set the command in docker-compose.yml