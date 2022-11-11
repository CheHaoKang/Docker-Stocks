# syntax=docker/dockerfile:1

FROM mysql/mysql-server:5.7

# RUN apt update && apt install vim iputils-ping default-mysql-client net-tools -y
RUN echo 'bind-address=0.0.0.0' >> /etc/my.cnf

# CMD [ "service", "mysql" , "restart" ]

# WORKDIR /stocks
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
# RUN apt update && apt install git iputils-ping default-mysql-client net-tools -y
# RUN git clone https://github.com/CheHaoKang/US_Stock.git
# RUN echo 'alias ll="ls -ltr"' >> ~/.bashrc
# CMD [ "/bin/bash" ]