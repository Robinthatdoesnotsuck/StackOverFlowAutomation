# ---- Base image ----
FROM python:3.12-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Add Poetry to PATH
ENV PATH="$POETRY_HOME/bin:$PATH"

# ---- Builder stage ----
FROM base AS builder

# Install system dependencies + Poetry
RUN apt-get update && apt-get install -y --no-install-recommends curl

WORKDIR /app

# Copy dependency files first (for better layer caching)
COPY requirements.txt ./

# Install dependencies only (no root package)
RUN pip install -r requirements.txt

# ---- Final stage ----
FROM base AS final

# Install Firefox and Geckodriver dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    firefox-esr \
    wget \
    ca-certificates \
    libdbus-glib-1-2 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxt6 \
    # Virtual display dependencies
    xvfb \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Geckodriver
ARG GECKODRIVER_VERSION=0.36.0
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v${GECKODRIVER_VERSION}/geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz" \
    && tar -xzf geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/geckodriver \
    && chmod +x /usr/local/bin/geckodriver \
    && rm geckodriver-v${GECKODRIVER_VERSION}-linux64.tar.gz

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application source
COPY . .

# Create a non-root user for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

# Set display for headless Firefox via Xvfb
ENV DISPLAY=:99

EXPOSE 8000

# Start Xvfb and then run the app
CMD ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x24 -ac &  python -m src.super_tester.app"]