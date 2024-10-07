# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies required for Poetry
RUN apt-get update && apt-get install -y curl && apt-get clean

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the system PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy the Poetry files to the container
COPY pyproject.toml poetry.lock* ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev 
    #poetry shell

# Copy the rest of the application code
COPY . .

# Expose the port for Airflow webserver
EXPOSE 8081

# Command to run Airflow
CMD ["airflow", "webserver"]

