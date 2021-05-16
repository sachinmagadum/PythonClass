import psycopg2
from psycopg2 import Error


def database_connection():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="postgres",
                                      password="Admin@123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="rohan_db")


        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        return connection
    except :
        print("Error while connecting to PostgreSQL")

def database_create_table_op():
    try:
        connection = database_connection()
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE mobile
                  (ID INT PRIMARY KEY     NOT NULL,
                  MODEL           TEXT    NOT NULL,
                  PRICE         REAL); '''
        # Execute a command: this creates a new table
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def database_insert_op(insert_query):
    try:
        connection = database_connection()
        # Create a cursor to perform database operations
        cursor = connection.cursor()

        # Execute a command: this creates a new table
        cursor.execute(insert_query)
        connection.commit()
        print("Data inserted successfully in PostgreSQL ")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            # cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


insert_query = '''INSERT INTO mobile (id, model, price)
                                VALUES (7, 'Apple', 1700),
                                (8, 'Samsung', 1600),
                                (9, 'Samsung', 1600);
         '''
# database_insert_op(insert_query)


def database_read():
    try:
        connection = database_connection()
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        read_table_query = '''select * from mobile;
         '''
        # Execute a command: this creates a new table
        cursor.execute(read_table_query)
        print("Result ", cursor.fetchall())
        connection.commit()
        print("Table created successfully in PostgreSQL ")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            # cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


database_read()