FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# Устанавливаем зависимости, включая email-validator для Pydantic
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir email-validator

COPY . .

# Создаем директорию для базы данных и инициализируем её
RUN mkdir -p /app/data

# Устанавливаем переменные окружения
ENV PORT=8000
ENV HOST="0.0.0.0"
ENV DEBUG=true

# Открываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["python", "start.py"] 