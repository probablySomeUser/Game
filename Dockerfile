FROM python:3.14.6-alpine

WORKDIR /app

COPY main.py weapons.py entities.py .

CMD ["python", "main.py"]