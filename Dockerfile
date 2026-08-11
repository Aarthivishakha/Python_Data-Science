FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /workspace
COPY . .
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir .
RUN addgroup --system app && adduser --system --ingroup app app \
    && mkdir -p /workspace/reports && chown -R app:app /workspace
USER app
CMD ["data-science", "--input", "data/sample.csv", "--output", "reports/report.json"]
