import psycopg2
from psycopg2 import Error


def postgres_connection() -> psycopg2.connect:

    connection = None

    try:
        connection = psycopg2.connect(user="dev",
                                      password="dev",
                                      host="localhost",
                                      port="5432",
                                      database="postgres_dev")

    except (Exception, psycopg2.DatabaseError) as error:
            print("Error while creating PostgreSQL table", error)

    finally: return connection

if __name__ == "__main__":
    postgres = get_db("postgres")
    postgres