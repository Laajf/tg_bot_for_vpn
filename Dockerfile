FROM python:3.8-slim

# Устанавливаем необходимые зависимости для pip
RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y openssh-client
# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости через pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . /app/

# Указываем команду для запуска приложения
CMD ["python", "app.py"]
