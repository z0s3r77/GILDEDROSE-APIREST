FROM python:3.10.0-alpine

COPY ./requirements.txt /flask_app/requirements.txt

WORKDIR /flask_app

RUN pip3 install -r requirements.txt

COPY . /flask_app

ENTRYPOINT [ "python3" ]

CMD ["controller/main.py" ]
