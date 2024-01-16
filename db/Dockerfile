FROM mysql:8.0

COPY ./my.cnf /etc/mysql/conf.d/my.cnf
COPY ./initdb/ /docker-entrypoint-initdb.d

RUN chmod 644 /etc/mysql/conf.d/my.cnf
RUN chmod -R 755 /docker-entrypoint-initdb.d

CMD ["mysqld"]
