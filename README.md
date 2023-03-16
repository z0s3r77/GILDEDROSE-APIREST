# PROYECTO-FLASK
**Indice**
- Requisitos
- Docker 
  - Dockerfile
  - docker build
  - docker run 

## Requisitos

Los requisitos para app están en el requirements.txt


## Docker
### Dockerfile

Para poder empezar a desarrollar el proyecto, uno de los requisitos era montar la aplicación sobre un contenedor de Docker. Para esto, una vez tenia una base muy pequeña del proyecto decidí hacer un Dockerfile.
Como sabran los lectores, el Dockerfile sirve para, apartir de este archivo con estructura __yaml__ introducir instrucciones sobre como actuará el contenedor. El archivo Dockerfile contiene la siguiente estructura:
````
    # IMAGEN DE PYTHON3.10 con Alpine, que es una version ligera de SO
    FROM python:3.10-alpine
    
    WORKDIR /app
    
    COPY requirements.txt /app
    RUN pip3 install --no-cache-dir -r requirements.txt
    
    COPY . /app
    
    EXPOSE 5000
    
    # Incio el server de Flask
    CMD ["python3", "controller/main.py"]
````
Como se puede ver, es un archivo sencillo, que por orden de instrucciones realiza las siguientes tareas:

    1. Descarga la imagen de python3.10-alpine
    2. Crea y establece como directorio de trabajo /app
    3. Copia, del directorio de este respositorio el fichero requirements.txt al directorio de trabajo del contenedor. 
    4. Instala las dependencias necesarias de requirements.txt
    5. Copia el contenido del directorio al contenedor (así ya tiene disponible todo el "tinglao")
    6. Abre el puerto 5000 del contenedor.
    7. Ejecuta dentro de este el comando "python3 controller/main.py", que es el que pone en marcha flask.

### docker build

Para montar la imagen basta con ejecutar el siguiente comando dentro del directorio donde está el Dockerfile:

````
    docker build -t flaskapirestolivanders .
````

Con ese comando le estamos indicando que "construya" una imagen a partir de las instrucciones del Dockerfile que se encuentra en "."(es decir, en ese mismo directorio) con el nombre flaskapirestolivanders.

### docker run 

Ahora montamos la aplicación, en mi caso compartiendo el directorio PROYECTO-FLASK con /app, para que Flask se ejecute desde el contenedor:

````
    docker run -p 5000:5000 -v C:\Users\Ipopd\Documents\FLASK\PROYECTO-FLASK\:/app/. --rm flaskolivanders
````
Esto me permite, seguir trabajando en el proyecto y, cuando se considera que se ha avanzado, se hace un commit de la imagen del contenedor. Esto con el fin de, al final del proyecto, tener la aplicación guardada y montada en una imagen y desplegarla en un contenedor.
