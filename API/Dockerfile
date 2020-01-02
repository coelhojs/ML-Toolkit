#API
FROM python:3.6
LABEL maintainer="Cristiano Coelho Souza <ccoelho.me@gmail.com>"
WORKDIR /api
ADD /. .
RUN pip3 install -r requirements.txt
RUN set FLASK_ENV=development && flask run --host=0.0.0.0