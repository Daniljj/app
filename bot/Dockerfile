FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY launcher_bot.py .

CMD ["python", "launcher_bot.py"]
