# import pymysql

# try:
#     connection = pymysql.connect(
#         host='your_host',       # e.g., 'localhost' or an IP address
#         user='your_username',   # e.g., 'root'
#         password='your_password', # e.g., 'password'
#         database='your_database'  # e.g., 'test_db'
#     )

#     with connection.cursor() as cursor:
#         # Execute an SQL query
#         cursor.execute("SELECT DATABASE();")

#         # Fetch the result
#         db = cursor.fetchone()
#         print(f"Connected to database: {db}")

# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     connection.close()
#     print("MySQL connection is closed")

import boto3

client = boto3.client('rds', region_name='us-east-1')
try:
    response = client.describe_db_instances()
    for db_instance in response['DBInstances']:
        print(f"DBInstanceIdentifier: {db_instance['DBInstanceIdentifier']}")
        print(f"Endpoint: {db_instance['Endpoint']['Address']}")
        print(f"Port: {db_instance['Endpoint']['Port']}")
        print(f"DBInstanceStatus: {db_instance['DBInstanceStatus']}")
        print("-" * 40)
except Exception as e:
    print(f"Error: {e}")
