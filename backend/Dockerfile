FROM nvidia/cuda:11.8.1-base-ubuntu24.04

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Install Python and system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.12 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Copy project
COPY ./app /app

# Expose the port your application runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]