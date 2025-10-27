FROM python:3.12-slim

WORKDIR /app

# Prevent Python from writing .pyc files and enable stdout/stderr unbuffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy only requirements first to leverage Docker cache
COPY requirements-prod.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements-prod.txt

# Copy application code
COPY . .

# Expose default port (Railway provides $PORT at runtime)
EXPOSE 8000

# Start the app with gunicorn (Railway provides $PORT env var).
# Use a shell to allow environment variable expansion. Provide a default port 8000
# in case $PORT is not set (useful for local testing).
CMD ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:${PORT:-8000}"]
