FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=8080

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml /app/
COPY uv.lock /app/

# Install deps with pip (using pip to read from pyproject)
RUN python -m pip install --upgrade pip \
    && pip install -r <(python - <<'PY'
import tomllib, sys
with open('pyproject.toml','rb') as f:
    data = tomllib.load(f)
deps = data.get('project',{}).get('dependencies',[])
print('\n'.join(deps))
PY
)

# Copy source
COPY . /app

# Create data dir for persistent volume (mounted in production)
RUN mkdir -p /data/uploads

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app", "--workers", "2", "--timeout", "120"]


