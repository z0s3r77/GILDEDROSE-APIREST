# IMAGEN DE PYTHON3.10 con Alpine, que es una version ligera de SO
FROM python:3.10-alpine

# Instalar dependencias necesarias
RUN apk add --no-cache build-base libffi-dev openssl-dev

# Configurar variables de entorno
ENV PYTHONPATH="/app/" \
    FLASK_APP="controller/main" \
    FLASK_ENV="production" \
    FLASK_RUN_HOST="0.0.0.0" \
    FLASK_RUN_PORT="5000"

# Directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt /app/
COPY . /app/

# Instalar dependencias de Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Exponer puerto 5000
EXPOSE 5000

# Iniciar el servidor de Flask
CMD ["flask", "run"]