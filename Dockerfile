# IMAGEN DE PYTHON3.10 con Alpine, que es una version ligera de SO
FROM python:3.10-alpine

ENV PYTHONPATH="/app/"
WORKDIR /app

COPY requirements.txt /app
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

# Incio el server de Flask
CMD ["flask", "--app", "controller/main", "run", "--host=0.0.0.0"]