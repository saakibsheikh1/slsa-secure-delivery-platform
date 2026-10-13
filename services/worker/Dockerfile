
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV LOG_LEVEL=INFO
ENV INTERVAL_SECONDS=30

WORKDIR /app

COPY app.py .

RUN useradd --system --uid 10001 appuser \
    && chown -R appuser:appuser /app

USER 10001

CMD ["python", "app.py"]
