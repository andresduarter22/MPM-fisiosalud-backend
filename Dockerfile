FROM python:3.9.17-alpine3.17
WORKDIR /srv
ADD ./requirements.txt /srv/requirements.txt
RUN apk add build-base linux-headers
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN apk add openssl-dev
RUN pip install uwsgi
COPY . .

# every time you change config.py you should update this encoded string :)
RUN printf "REJfVVNFUl9OQU1FID0gJ2FkbWluJwpEQl9VU0VSX1BBU1NXT1JEID0gJ3BhdGl0bzIyJwpEQl9IT1NUX05BTUUgPSAnZGInCkRCX1BPUlQgPSAyNzAxNwpEQl9EQVRBQkFTRSA9ICdtcG1fZmlzaW9zYWx1ZCcKCkpXVF9QUklWQVRFX0tFWSA9ICJZSGZORHZ6THo3b1ZZYVNhVzdEWWNSUmlFIgpKV1RfQVVUSF9EVVJBVElPTiA9IDEwICogNjAKSldUX1JFRlJFU0hfRFVSQVRJT04gPSAzICogNjAgKiA2MApKV1RfQUxHT1JJVEhNID0gIkhTNTEyIgpKV1RfSVNTVUVSID0gImh0dHBzOi8vdGVzdC5kb21haW4uY29tIg==" | base64 -d > config.py
RUN dos2unix ./run.sh
EXPOSE 443