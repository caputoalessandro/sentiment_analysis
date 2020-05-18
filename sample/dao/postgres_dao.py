from abc import ABC
import psycopg2
from psycopg2 import Error
from sample.dao.dao_abc import DAO
from sample.dao.dao_factory import get_db

class postgresDAO(DAO):
    pass
#     db_type = "postgres"
#
#     def __init__(self):
#         db_name
#
#     def create_schema(self, schema : Sql):
#
#         try:
#             connection = psycopg2.connect(user="dev",
#                                           password="dev",
#                                           host="localhost",
#                                           port="5432",
#                                           database="postgres_dev")
#
#             cursor = connection.cursor()
#
#             create_table_query = schema.sql
#
#             cursor.execute(create_table_query)
#             connection.commit()
#             print("Table created successfully in PostgreSQL ")
#
#         except (Exception, psycopg2.DatabaseError) as error:
#             print("Error while creating PostgreSQL table", error)
#         finally:
#             # closing database connection.
#             if (connection):
#                 cursor.close()
#                 connection.close()
#                 print("PostgreSQL connection is closed")
#
#
#     def insert_word(self, connection):
#
#         try:
#             connection = psycopg2.connect(user="postgres",
#                                           password="pass@#29",
#                                           host="127.0.0.1",
#                                           port="5432",
#                                           database="postgres_db")
#
#             cursor = connection.cursor()
#
#             postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
#             record_to_insert = (5, 'One Plus 6', 950)
#             cursor.execute(postgres_insert_query, record_to_insert)
#
#             connection.commit()
#             count = cursor.rowcount
#             print(count, "Record inserted successfully into mobile table")
#
#         except (Exception, psycopg2.Error) as error:
#             if (connection):
#                 print("Failed to insert record into mobile table", error)
#
#         finally:
#             # closing database connection.
#             if (connection):
#                 cursor.close()
#                 connection.close()
#                 print("PostgreSQL connection is closed")
#         pass
#
# if __name__ == "__main__":
#     postgres = get_db("postgres")
#     postgres
