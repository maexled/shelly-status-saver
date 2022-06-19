FROM python:3.9-alpine

WORKDIR /mystrom

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "-m", "main"]