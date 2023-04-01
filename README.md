# PROYECTO-FLASK
**Indice**
- Descripción técnica
- Requisitos del Sistema
- Librerias utilizadas
  - Funcionales
    - Flask
    - flask-restful
    - PyMongo
  - Desarrollo
    - Pytest
    - Coverage
    - Bandit
    - Tox
    - pylint
    - isort
- Instalación
- Documentación API REST
  - Endpoints
  - Ejemplos de uso
    - /items/all
    - /items/insert
    - /items/update/<id:int>
    - /items/delete/<id:int>
    - /db/initialize
    - /db/update
    - /db/drop
- Metodología de desarrollo
    - TDD
    - CI/CD
- Docker 
  - Dockerfile
  - docker build
  - docker run

## Descripción

La API Rest de GildedRose tiene como objetivo simular todo el inventario de una tienda de items mágicos, cuyo valor de calidad varía según sus días de caducidad y según el tipo de objeto. A rasgos generales, la aplicación se conecta mediante Flask a MongoAtlas y sirve el contenido de la base de datos, si el usuario lo desea, puede actualizar todo el inventario. 

Adicionalmente, se han añadido más funcionalidades, como insertar objetos nuevos, actualizarlos, inicia una base de datos nueva, etc.

Para poder ilustrar mejor la arquitectura de la API, se ha facilitado el siguiente diagrama:

![modulosFlask drawio](https://user-images.githubusercontent.com/80277545/229276115-8c228434-fb1d-42ed-ad37-7df1a5639d00.png)

- La __CAPA DE PRESENTACÍON__ serían los endpoints de Flask, las direcciones URL que usamos para poder enviar peticiones HTTP. La aplicación se inicia mediante el archivo __main.py__ pero consume del resto de modulos que hay en el directorio __/controller__.
- La __CAPA LÓGICA__ sería el modulo __service.py__. Este modulo es invocado por Flask, es el encargado de realizar las operaciones lógicas, ya sea hacer peticiones a la base de datos o modificar o actualizar objetos. Para actualizar los objetos, se hace servir de la lógica de cada tipo de item guardada en __/domain/items__ . 
- La __CAPA DE ACCESO A DATOS__ , sería el modulo __MongoRepository.py__ , que sería el encargado de hacer las peticiones a la base de datos y realizar el __CRUD__. 

## Requisitos del Sistema
Tener instalado: 

  - Python 3.10
  - pip3
  - Git

Con esto, ya estaría todo listo para ejecutar la aplicación.

## Librerias utilizadas
### Funcionales
#### Flask
La API rest está montada sobre Flask, un micro framework de Python que nos permite montar un servicio web de una manera 
rapida. Por defecto, Flask utiliza el puerto 5000 por defecto. (en la aplicación se usa este mismo). Por defecto, Flask utiliza el servidor web integrado llamado "Werkzeug" para escuchar en el puerto 5000. Werkzeug es una biblioteca WSGI (Web Server Gateway Interface) escrita en Python que proporciona una base para el desarrollo de aplicaciones web. Es uno de los tres pilares de Flask.

#### Flask-restful
Al ser una API RESTful, he utilizado la extension de Flask, __Flask-Restful__. Con esta extensión se pueden definir de manera sencilla las rutas, recursos y operaciones HTTP(GET,POST,PUT, etc.) que estarán disponibles.

#### PyMongo
PyMongo es una librería de Python que nos permite conectarnos a una base de datos MongoDB y realizar operaciones CRUD (Create, Read, Update, Delete).


### Desarrollo
#### Pytest
Pytest es un framework que usado para implementar la metodología TDD a la aplicación. Permite escribir test con Python de una manera eficiente y sencilla. 
Todos los ficheros test están en el directorio __/test__.

#### Coverage
Coverage es otro framework de desarrollo, que la he utilizado para medir la cobertura del código durante las implementación de los test.
De este modo, me aseguro que todo el código está bajo control.

#### Bandit
También en lo que se refiere al desarrollo, se ha utilizado Bandit, que es un framework de análisis de seguridad de código fuente exclusivo de Python.
En otras palabras, esta herramienta trata de identificar posibles vulnerabilidades en el código fuente.


#### Tox 
Tox es una herramienta que automatiza la configuración y ejecución de pruebas en múltiples entornos para proyectos Python. Con Tox, puedes definir diferentes entornos de prueba en un archivo de configuración llamado __tox.ini__.
Cada entorno puede tener diferentes versiones de Python, paquetes de dependencias y comandos de prueba. Esto te permite asegurarte de que tu proyecto funciona correctamente en diferentes configuraciones de entorno de prueba.

#### Pylint
Pylint es una herramienta de análisis estático de código abierto para Python. Pylint se puede usar para detectar errores en el código, así como para evaluar la calidad del código.

#### Isort
Isort es una herramienta de ordenación de importaciones de Python. Es una herramienta de línea de comandos que puede ser usada para ordenar automáticamente las importaciones en Python. 

## Instalación

__ACLARACIÓN:__ También está la posibilidad de ejecutar la aplicación sin necesidad de clonar este respositorio. Para esto siga el siguiente manual:
[Manual de instalación de la aplicación en un contenedor Docker](https://hub.docker.com/r/z0s3r77/flaskapirestolivanders)


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
Por último, necesitas exportas las variables de entorno de Mongo Atlas, para ello necesitarás una __KEY__ para usar la API de atlas y __la dirección del cluster__.
Esta información la puedes encontrar en tu página de Mongo Atlas.
  -  Visita: https://cloud.mongodb.com ,en caso de no tener cuenta, puedes registrarte de forma gratuita. Dirigete a al siguiente apartado:
      - Elige la opción "Connect your application" y elige la opción "Python" y copia la dirección del cluster rellenando la url con tu usuario y contraseña.
    ![imagen](https://user-images.githubusercontent.com/80277545/227264121-8172a35a-ae9a-492d-a2d0-081c0be9d8a2.png)
  - Para obtener la KEY, debes dirigirte a la parte de Data API y crear una nueva KEY:
    ![imagen](https://user-images.githubusercontent.com/80277545/227264312-4c668a4e-1ed3-4151-998d-b39f26de974e.png)
  - Y tomar la KEY generada.
    ![imagen](https://user-images.githubusercontent.com/80277545/227264458-6e41a425-f852-4082-afab-6fdbaf1b3b8c.png)
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
Si todo ha ido bien, deberías ver el siguiente mensaje:
```
  {
    "Message": "Flask is Running!"
  }
```


## Documentación API REST
### Endpoints

La API consta de los siguientes endpoints:

| Endpoint               | Método | Descripción                                                |
|------------------------|-------|------------------------------------------------------------|
| /                      | GET   | Devuelve un mensaje de bienvenida                          |
| /items/<id:int>        | GET   | Devuelve un item por su id                                 |
| /items/update/<id:int> | POST  | Actualiza un item por su id                                |
| /items/delete/<id:int> | DELETE | Elimina un item por su id                                  |
| /items/insert          | PUT   | Recibe un documento JSON y lo inserta a la DB              |
| /items/all             | GET   | Devuelve todos los items de la DB                          |
| /db/initialize         | GET   | Inicializa la DB con los datos del fichero __itemList.py__ |
| /db/update             | GET   | Ejecuta el método __updateQuality()__ en todos los items   |
| /db/drop               | GET   | Elimina la DB                                              |

### Ejemplos de uso
Aclaración: Es importante, que antes de ejecutar las peticiones realices la petición de inicialización de la DB, para ello, debes ejecutar el siguiente comando:
```
  curl -X GET http://localhost:5000/db/initialize
```
A continuation, se muestran algunos ejemplos de uso de la API REST con el comando __curl__:

#### GET /
```
  curl -X GET http://localhost:5000
  
  OK 200: {
    "Message": "Flask is Running!"
    }
    
  
```
#### GET /items/1
```
  curl -X GET http://localhost:5000/items/1
  
  200 OK: {
    "name": "+5 Dexterity Vest",
    "sell_in": 10,
    "quality": 20
    }
   
  404 NOT FOUND: {
    "Error Message": "The item with id 1 not exist"
  } 
```
#### POST /items/update/1
```
  curl -X POST http://localhost:5000/items/update/1
  
  200 OK: {
    "Message": "The item have been updated"
  }
  
  404 NOT FOUND: {
    "Error Message": "The item with id 1000 not exist"
  }
  
```
#### DELETE /items/delete/1
```
  curl -X DELETE http://localhost:5000/items/delete/100
  
    202 ACCEPTED: {
        "Message": "The item has been deleted with id 100"
    }
    
    404 NOT FOUND: {
        "Message": "The item is not in the DB"
    }
  
```
#### PUT /items/insert
```
  curl -X PUT -H "Content-Type: application/json" -d '{"_id": 111, "name":"Aged Brie","sell_in":2,"quality":0}' http://localhost:5000/items/insert
  
    201 CREATED: {
        "Message": "The item has been introduced with id 111"
    }
    
    200 OK:  (Esto pasa si el item ya se encontraba en la DB y se ha actualizado)
    
  curl -X PUT -H "Content-Type: application/json" -d '{"_id": 111, "name":"Aged Brie","sell_in":2,"quality":0, "quality2": 12}' http://localhost:5000/items/insert
    
  400 BAD REQUEST: {
    "message": "The browser (or proxy) sent a request that this server could not understand."
  }
```
#### GET /items/all
```
  curl -X GET http://localhost:5000/items/all
  
  200 OK : Devuelve todos los items de la DB en formato JSON
  404 NOT FOUND: {
    "Error Message": "The items are not in the DB, intialize with /db/initialize"
  }
  
```
#### GET /db/initialize
```
  curl -X GET http://localhost:5000/db/initialize
  200 OK: {
    "Message": "GildedRose is Open!"
  }
```
#### GET /db/update
```
  curl -X GET http://localhost:5000/db/update
  404 NOT FOUND: {
    "Error Message": "The items are not in the DB, intialize with /db/initialize"
  }
  200 OK: Devuelve todos los items de la DB en formato JSON
```
#### GET /db/drop
```
  curl -X GET http://localhost:5000/db/drop
    200 OK: {
        "Message": "GildedRose is Closed!"
    }
```

## Metodología de desarrollo
### TDD
Para desarrollar la API REST, decidí utilizar la metodología TDD (Test Driven Development). Esta metodología consiste en desarrollar el código de la aplicación, basándose en los test que se van creando. Para ello, se crean los test primero, y luego se desarrolla el código para que pase los test. (__Aclaración__: En algún caso se dificultó está práctica y primero se desarrollaba el código y luego se testeaba) 

### CI/CD
Para la integración continua, decidí utilizar __GitHub Actions__. Este servicio de __GitHub__ permite crear workflows, que son una serie de pasos que se ejecutan en el servidor de __GitHub__ cuando se realiza un push (u otra actividad) a un repositorio. En este caso, se ha generado un workflow que se ejecuta cuando se realiza un push a la rama __dev__. Este workflow se encarga de ejecutar los test de la aplicación, de este modo
me aseguraba que el código que estaba subiendo a la rama __dev__ pasaba los test y no comprometía las funcionalidades. Por otro lado, como CD interpreté que la puesta en producción sería subir el codigó a una imagen de Docker Hub, para ello en la rama master hay un workflow que hace este trabajo automáticamente.

## Docker
### Dockerfile

Para poder empezar a desarrollar el proyecto, uno de los requisitos era montar la aplicación sobre un contenedor de Docker. Para esto, una vez tenia una base muy pequeña del proyecto decidí hacer un Dockerfile.
Como sabran los lectores, el Dockerfile sirve para, a partir de este archivo con estructura __yaml__ introducir instrucciones sobre como actuará el contenedor. El archivo Dockerfile contiene la siguiente estructura:
````
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
````
Como se puede ver, es un archivo sencillo, que por orden de instrucciones realiza las siguientes tareas:

    1. Descarga la imagen de python3.10-alpine
    2. RUN apk add --no-cache build-base libffi-dev openssl-dev: se instalan las dependencias necesarias para compilar algunas bibliotecas de Python, específicamente build-base, libffi-dev y openssl-dev.
    3. ENV PYTHONPATH="/app/" FLASK_APP="controller/main" FLASK_ENV="production" FLASK_RUN_HOST="0.0.0.0" FLASK_RUN_PORT="5000": se establecen algunas variables de entorno útiles para la aplicación. 
    4. WORKDIR /app: se establece el directorio de trabajo para la aplicación en /app.
    5. COPY requirements.txt /app/ y COPY . /app/: se copian los archivos necesarios para la aplicación. En particular, requirements.txt es copiado al directorio /app.
    6. RUN pip3 install --no-cache-dir -r requirements.txt: se instalan las dependencias de Python especificadas en el archivo requirements.txt.
    7. EXPOSE 5000: se expone el puerto 5000 para que se pueda acceder a la aplicación Flask.
    8. CMD ["flask", "run"]: se ejecuta el comando flask run para iniciar el servidor de Flask.

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
Con este comando le estamos indicando que "ejecute" un contenedor a partir de la imagen flaskapirestolivanders, que expone el puerto 5000 del contenedor al puerto 5000 del host, que monta el directorio PROYECTO-FLASK en /app del contenedor, que elimine el contenedor cuando se detenga y que se ejecute en segundo plano.
Así puedo trabajar con la aplicación en el host y que Flask se ejecute en el contenedor. En caso de querer trabajar con más compañeros, tan solo debo pasarles la imagen de Flask.

