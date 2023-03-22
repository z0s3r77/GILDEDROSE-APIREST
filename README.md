# PROYECTO-FLASK
**Indice**
- Descripción 
- Requisitos
  - Funcionales
    - Flask
    - flask-restful
  - Desarrollo
    - Pytest
    - Coverage
    - Bandit
    - Tox
- Instalación
- Documentación API REST
- Metodología de desarrollo
- Docker 
  - Dockerfile
  - docker build
  - docker run

## Descripción
## Requisitos
### Funcionales
#### Flask
La API rest está montada sobre Flask, un micro framework de Python que nos permite montar un servicio web de una manera 
rapida. Por defecto, Flask utiliza el puerto 5000 por defecto. (en la aplicación se usa este mismo). Por defecto, Flask utiliza el servidor web integrado llamado "Werkzeug" para escuchar en el puerto 5000. Werkzeug es una biblioteca WSGI (Web Server Gateway Interface) escrita en Python que proporciona una base para el desarrollo de aplicaciones web. Es uno de los tres pilares de Flask.

#### Flask-restful
Al ser una API RESTful, he utilizado la extesión de Flask , __Flask-Restful__. Con esta extensión se pueden definir de manera sencilla las rutas, recursos y operaciones HTTP(GET,POST,PUT, etc.) que estarán disponibles.

### Desarrollo
#### Pytest
Pytest es un framework que usado para implementar la metodología TDD a la aplicación. Permite escribir test con Python de una manera eficiente y sencilla. 
Todos los ficheros test están en el directorio __/test__.

#### Coverage
Coverage es otro framework de desarrollo , que la he utilizado para medir la cobertura del código durante las implementación de los test.
De este modo, me aseguro que todo el código está bajo control.

#### Bandit
También en lo que se refiere al desarrollo, se ha utilizado Bandit, que es un framework de análisis de seguridad de código fuente exclusivo de Python.
En otras palabras, esta herramienta trata de identificar posibles vulnerabilidades en el código fuente.


#### Tox 
Tox es una herramienta que automatiza la configuración y ejecución de pruebas en múltiples entornos para proyectos Python. Con Tox, puedes definir diferentes entornos de prueba en un archivo de configuración llamado __tox.ini__. Cada entorno puede tener diferentes versiones de Python, paquetes de dependencias y comandos de prueba. Esto te permite asegurarte de que tu proyecto funciona correctamente en diferentes configuraciones de entorno de prueba.

## Instalación
Primero debes clonar el repositorio:
```
  git clone https://github.com/z0s3r77/PROYECTO-FLASK
```
Una vez clonado el repositorio, debes iniciar un entorno virtual de Python. Para ello, en el directorio del proyecto, ejecuta el siguiente comando:
```
  python3 -m venv venv
```
Una vez creado el entorno virtual, debes activarlo:
```
  source venv/bin/activate
```
Ahora, debes instalar las dependencias del proyecto:
```
  pip3 install -r requirements.txt
```
Antes de iniciar la aplicación, debes establecer las dos variables de entorno que necesita la aplicación. Para ello, debes ejecutar los siguientes comandos:
```
  export FLASK_APP=controller/main.py
  export FLASK_RUN_HOST=0.0.0.0
```
Por último, necesitas exportas las variables de entorno de Mongo Atlas, para ello necesitarás una __KEY__ para la usar la API de atlas y __la dirección del cluster__.
Esta información la puedes encontrar en tu página de Mongo Atlas.
  -  Visita: https://cloud.mongodb.com ,en caso de no tener cuenta, puedes registrarte de forma gratuita. Dirigete a al siguiente apartado:
    [imagen connect]
  - Elige la opción "Connect your application" y elige la opción "Python" y copia la dirección del cluster rellenando la url con tu usuario y contraseña.
    [imagen python]
  - Para obtener la KEY, debes dirigirte a la parte de Data API y crear una nueva KEY:
    [imagen key]
  - Y tomar la KEY generada.
    [imagen key2]
Ahora, te diriges a tu entorno (venv) y ejecutas los siguientes comandos:
```
  export KEY="La KEY que has obtenido de Mongo Atlas"
  export ATLAS="La dirección del cluster de Mongo Atlas con tu usuario y contraseña
```

Con esto, ya estaría todo listo para ejecutar la aplicación. Para ello, debes ejecutar el siguiente comando:
```
  flask --app controller/main run --host=0.0.0.0
```

Para verificar que la API REST está funcionando, dirígete a tu navegador y escribir la siguiente dirección:
```
  http://localhost:5000
```

## Documentación API REST



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


docker run -e KEY="SwVPwadBrjuOJcUQrh887SGLLUq9IGo2e6fFOPo0lQumOkRNW0xTC5v3YROR1S3T" -e ATLAS="mongodb+srv://sestacio:trancas24@sandbox.dcnt9qr.mongodb.net/test?retryWrites=true&w=majority" -p 5000:5000 --rm  -v C:\Users\Ipopd\Documents\FLASK\PROYECTO-FLASK\:/app/.   flaskapirestolivandersv2