import os
import logging
import mysql.connector
from dotenv import load_dotenv
logging.basicConfig(level = logging.INFO)

class DB:

    logger = logging.getLogger("db_logger")
    def __init__(self):
        load_dotenv()
        self.HOST = os.environ.get('HOST')
        # self.USER = os.environ.get('USERNAME')
        self.USER = os.environ.get('USER')
        self.PASSWORD = os.environ.get('PASSWORD')
        self.db = 'Fitness'

        self.config = {
            "host": self.HOST,
            "user": self.USER,
            "passwd": self.PASSWORD,
            "database": self.db
        }
        
        self.mysqlcxn = None

    def __enter__(self):
        try:
            self.mysqlcxn = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            if err.errno == 2003:
                self.mysqlcxn = None
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.mysqlcxn is not None and self.mysqlcxn.is_connected():
            self.mysqlcxn.close()

    def cursor(self, dictionary=True):
        cursor = self.mysqlcxn.cursor(dictionary=True)
        return cursor
