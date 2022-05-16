import psycopg2
from config import *

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)

connection.autocommit = True

# with connection.cursor() as cursor:
#     cursor.execute(
#         """SELECT * FROM users"""
#     )
#     print(cursor.fetchall())


# with connection.cursor() as cursor:
#     cursor.execute(
#         """DROP TABLE data"""
#     )
#
# print("[INFO ] Table droped seccessfully")

# with connection.cursor() as cursor:
#     cursor.execute(
#         """CREATE TABLE users(
#                 id serial PRIMARY KEY,
#                 user_id serial8 NOT NULL,
#                 user_name varchar(100),
#                 user_surname varchar(100),
#                 username varchar(100));"""
#     )
#
# print("[INFO ] Table created successfully")
#

# with connection.cursor() as cursor:
#     cursor.execute(
#         """CREATE TABLE data(
#                 id serial PRIMARY KEY,
#                 user_id serial8 NOT NULL,
#                 username varchar(100),
#                 last_time serial,
#                 technology varchar(50),
#                 civilization varchar(50),
#                 koord varchar(50),
#                 resource serial,
#                 army serial,
#                 killpoints serial,
#                 progress varchar(1000));"""
#     )
#
# print("[INFO ] Table created successfully")