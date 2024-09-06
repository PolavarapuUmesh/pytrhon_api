# import psycopg2
# from psycopg2 import sql

# # Database connection configuration
# db_config = {
#     'dbname': 'postgres',             # Default database to connect to
#     'user': 'postgres_01',            # Your PostgreSQL username
#     'password': 'G6CDlIHxuY0wFRaVxI4L',      # Your PostgreSQL password
#     'host': 'database-1.chcsskyi4wa1.us-east-1.rds.amazonaws.com',  # Your PostgreSQL host
#     'port': '5432'                    # Default PostgreSQL port
# }

# def connect_db():
#     """Establishes and returns a connection to the PostgreSQL database."""
#     try:
#         connection = psycopg2.connect(**db_config)
#         print("Connected to the PostgreSQL database successfully")
#         return connection
#     except psycopg2.OperationalError as e:
#         print(f"OperationalError: {e}")
#     except psycopg2.ProgrammingError as e:
#         print(f"ProgrammingError: {e}")
#     except psycopg2.Error as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#     return None

# if __name__ == "__main__":
#     conn = connect_db()

#     if conn:
#         print("Connection was successful!")
#         conn.close()
#     else:
#         print("Failed to connect to the database.")


import psycopg

# Building the database connection

    connection = psycopg.connect(
        dbname="database-1",
        user="postgres_01",
        password="G6CDlIHxuY0wFRaVxI4L",
        host="database-1.chcsskyi4wa1.us-east-1.rds.amazonaws.com",
        port="5432"
    )
    print("Successfully connected to database")

# Creating a cursor
cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")
Datasets = cursor.fetchall()

for data in datasets:
    print(row)

cursor.close()
