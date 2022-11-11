# syntax=docker/dockerfile:1

# FROM ubuntu/mysql

# RUN apt update && apt install python3 python3-pip mysql-server vim git iputils-ping default-mysql-client net-tools -y
# RUN service mysql start
# CMD [ "/bin/bash" ]

FROM python:3.8-slim-buster

WORKDIR /indices

RUN apt update && apt install vim iputils-ping default-mysql-client net-tools -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "--debug", "run", "--host=0.0.0.0"]

# WORKDIR /stocks
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
# RUN apt update && apt install git iputils-ping default-mysql-client net-tools -y
# RUN git clone https://github.com/CheHaoKang/US_Stock.git
# RUN echo 'alias ll="ls -ltr"' >> ~/.bashrc
# CMD [ "/bin/bash" ]