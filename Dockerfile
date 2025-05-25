# использовать официальный python образ
FROM python:3.11-slim

# рабочая директория в контейнере
WORKDIR /app

# скопировать файлы зависимостей
COPY requirements.txt .

# установить зависимости
RUN pip install --no-cache-dir -r requirements.txt

# скопировать весь проект
COPY . .

# собрать статику (если нужно)
RUN python manage.py collectstatic --noinput

# миграции базы данных
RUN python manage.py migrate

# expose порт (django по умолчанию 8000)
EXPOSE 8000

# запуск сервера (можно заменить на gunicorn)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
