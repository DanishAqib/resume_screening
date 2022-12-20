import psycopg2

from table_queries import users_table

from postgres import PostgresConnection

def create_tables():
     with PostgresConnection() as connection:
        cursor = connection.cursor()
        table_queries = [
            users_table
        ]
        for query in table_queries:
            try:
                cursor.execute(query)
            except psycopg2.DatabaseError as e:
                print(e)
                pass