import psycopg2
from sample.db_managment.postgres_connection import postgres_connect


def create_tables(schema='db_managment/schema.sql'):
    try:
        connection = postgres_connect()

        cursor = connection.cursor()

        create_table_query = open(schema, 'r')

        cursor.execute(create_table_query.read())

        connection.commit()

        print("Table created successfully in PostgreSQL ")

    except (Exception, psycopg2.DatabaseError) as error:
        connection.rollback()
        print("Error while creating PostgreSQL table", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")
