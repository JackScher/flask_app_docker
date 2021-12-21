FROM python:3.8.2-alpine

COPY requirements.txt ./requirements.txt

RUN apk add --no-cache \
    postgresql-libs \
    libstdc++

RUN apk --no-cache add --virtual build-dependencies \
    build-base \
    gcc \
    libffi-dev \
    postgresql-dev \
    && rm -rf .cache/pip

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r ./requirements.txt

COPY main.py ./main.py
COPY models.py ./models.py 
COPY schemas.py ./schemas.py
COPY config.py ./config.py

ENTRYPOINT FLASK_APP=./main.py flask run --host=0.0.0.0 --port=80
