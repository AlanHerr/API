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

# Start the app with gunicorn (Railway provides $PORT env var)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]
