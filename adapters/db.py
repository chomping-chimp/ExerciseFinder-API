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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self._conn.commit()
        else:
            self._conn.rollback()
        self._conn.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self._conn.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self._conn.close()

    def execute(self, sql, params=None):
        self._cursor.execute(sql, params or ())

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()