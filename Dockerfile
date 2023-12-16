FROM python:3.9.17-alpine3.17
WORKDIR /srv
ADD ./requirements.txt /srv/requirements.txt
RUN apk add build-base linux-headers
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY . .

# every time you change config.py you should update this encoded string :)
RUN printf "" | base64 -d > config.py

EXPOSE 5000