FROM postgres:16
ENV POSTGRES_DB=gopu
ENV POSTGRES_USER=ceose
ENV POSTGRES_PASSWORD=agentic
COPY init.sql /docker-entrypoint-initdb.d/
