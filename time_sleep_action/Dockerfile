FROM python:3.9-slim
WORKDIR /time_sleep_action

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование файлов проекта
COPY . .

# Запуск приложения
CMD ["python", "tasks.py"]
