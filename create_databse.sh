#! /bin/bash

# import psycopg2

# conn = psycopg2.connect(
#    database="postgres", user='admin', password='pass', host='127.0.0.1', port= '5432'
# )
# conn.autocommit = True
# cursor = conn.cursor()
# sql = '''CREATE database mydb''';
# cursor.execute(sql)
# print("Database created successfully........")
# conn.close()

# # cursor = conn.cursor()
# # cursor.execute("select version()")
# # data = cursor.fetchone()
# # print("Connection established to: ",data)
# # conn.close()

# sudo -u postgres psql -c 'alter user kuser with createdb' postgres
# sudo -u postgres createdb -O kuser kdb
# sudo -u postgres dropdb -f 'database';

#### sh ./create_databse.sh ###

echo "ReCreating Database and User"

sudo -u postgres psql -c "DROP DATABASE IF EXISTS database" postgres;
sudo -u postgres psql -c "DROP ROLE ADMIN" postgres;
sudo -u postgres psql -c "CREATE DATABASE database" postgres;
sudo -u postgres psql -c "CREATE USER admin WITH PASSWORD 'pass'" postgres;
sudo -u postgres psql -c "ALTER ROLE admin SET client_encoding TO 'utf8'" postgres;
sudo -u postgres psql -c "ALTER ROLE admin SET default_transaction_isolation TO 'read committed'" postgres;
sudo -u postgres psql -c "ALTER ROLE admin SET timezone TO 'UTC'" postgres;
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE database TO admin" postgres;
