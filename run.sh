#!/bin/sh


uwsgi --master --https 0.0.0.0:443,mpmlf.crt,mpmlf.key -p 4 --log-master -w wsgi:app