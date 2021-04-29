import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

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
        self.connection = db_connection(HOST, USER, PASSWORD, 'Fitness')
    
    def db_get(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        myresult = cursor.fetchall()
        return myresult