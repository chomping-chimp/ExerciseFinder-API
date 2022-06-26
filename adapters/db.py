import os
import logging
import mysql.connector
from dotenv import load_dotenv
logging.basicConfig(level = logging.INFO)

class Database:

    logger = logging.getLogger("db_logger")

    def __init__(self):
        load_dotenv()
        self.HOST = os.environ.get('HOST')
        self.USER = os.environ.get('USER')
        self.PASSWORD = os.environ.get('PASSWORD')
        self.db = 'Fitness'

        self.config = {
            "host": self.HOST,
            "user": self.USER,
            "passwd": self.PASSWORD,
            "database": self.db
        }
        self._conn = mysql.connector.connect(**self.config)
        self._cursor = self._conn.cursor(dictionary=True)

    def get_connection(self):
        return self._conn.cursor()
