#!/bin/sh

openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem -subj "/C=SI/ST=La Paz/L=La Paz/O=Fisiosalud/OU=IT Department/CN=www.example.com"

#uwsgi --master --https 0.0.0.0:443,cert.pem,key.pem -p 4 -w wsgi:FisiosaludAPI.app

uwsgi --master --https 0.0.0.0:5000,cert.pem,key.pem -p 4 --log-master -w wsgi:app