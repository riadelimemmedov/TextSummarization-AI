# pull official base image
FROM postgres:16

# run create.sql on init(The /docker-entrypoint-initdb.d directory is a special directory in the PostgreSQL image that automatically executes any SQL files placed in it during the initialization process. This allows you to initialize the database with custom SQL scripts)
ADD create.sql /docker-entrypoint-initdb.d 

