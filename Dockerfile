# Use an official Python image
FROM python:3.10-slim

# Basic environment setup
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DISPLAY=:99

# Install Chrome and essential dependencies only
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy files and install package
COPY . /app
RUN pip install --no-cache-dir .

# Expose port and run
EXPOSE 8000
CMD ["python", "-m", "v3cap"]
