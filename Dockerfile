FROM python:3-slim-buster

WORKDIR /mystrom

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "./main.py"]