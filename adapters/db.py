import os
import logging
import mysql.connector
from dotenv import load_dotenv
logging.basicConfig(level = logging.INFO)

class Database:

    logger = logging.getLogger("db_logger")

    def __init__(self):
        load_dotenv()
        self.HOST = os.environ.get('DB_HOST')
        self.USER = os.environ.get('DB_USER')
        self.PASSWORD = os.environ.get('DB_PASSWORD')
        self.db = 'Fitness'

        self.config = {
            "host": self.HOST,
            "user": self.USER,
            "passwd": self.PASSWORD,
            "database": self.db
        }
        self._conn = mysql.connector.connect(**self.config)

    def get_connection(self, cursor_type=None):
        
        if not cursor_type:
            cursor = False
        else:
            cursor = True

        return self._conn.cursor(dictionary=cursor)
