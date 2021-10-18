import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
HOST = os.environ.get('HOST')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
# Need to toggle the dotenv import between the dev and prod env

def db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except:
        print(f"[DEBUG] - Error connecting to Database")
    return connection

class DB:

    def __init__(self):
        pass
    
    def db_get(self, query):
        connection = db_connection(HOST, USER, PASSWORD, 'Fitness')
        cursor = connection.cursor()
        cursor.execute(query)
        myresult = cursor.fetchall()
        connection.close()
        return myresult
