FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py producer.py consumer.py .

CMD ["python", "main.py"]
