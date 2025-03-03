# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . .

# Создаем пользователя без прав root
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Открываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "table_project.wsgi:application"] 