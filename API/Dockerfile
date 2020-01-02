#API
FROM python:3.6
LABEL maintainer="Cristiano Coelho Souza <ccoelho.me@gmail.com>"
WORKDIR /api
ENV FLASK_ENV="development"
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ADD /. .
RUN pip3 install -r requirements.txt
CMD ["flask", "run"]