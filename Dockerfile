FROM python:3.9-slim

WORKDIR /mystrom

COPY requirements.txt ./

RUN apt-get update && \
    apt-get -y install libpq-dev gcc && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "-m", "main"]