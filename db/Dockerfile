FROM mysql:8.0

COPY ./my.cnf /etc/mysql/conf.d/my.cnf
COPY ./initdb/ /docker-entrypoint-initdb.d

RUN rm -rf /var/lib/mysql/*
RUN mysqld --initialize
