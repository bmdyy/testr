FROM debian:latest

RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask

COPY ./ /app

ENTRYPOINT ["python3","/app/app.py"]