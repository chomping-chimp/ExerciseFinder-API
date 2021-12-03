import os
import logging
import mysql.connector
from dotenv import load_dotenv
logging.basicConfig(level = logging.INFO)

class DB:

    def __init__(self, db_name='Fitness'):
        load_dotenv()
        self.HOST = os.environ.get('HOST')
        #self.USER = os.environ.get('USERNAME')
        self.USER = os.environ.get('USER')
        self.PASSWORD = os.environ.get('PASSWORD')

        self.db = db_name
        self.logger = logging.getLogger("db_logger")
    
    def create_connection(self, db_name='Fitness'):
        """ Creates DB Connection using the default database

        Args:
            db_name (str, optional): Database to connect to. Defaults to 'Fitness'.

        Returns:
            connection: MySQL connection Object
        """
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.HOST,
                user=self.USER,
                passwd=self.PASSWORD,
                database=db_name
            )
            self.logger.info("MySQL Database connection successful")
        except:
            self.logger.warn("[DEBUG] - Error connecting to Database")

        return connection

    def db_get(self, query, fetch_one=False):
        """ Method to be used to execute commands to the DB

        Args:
            query (string): Query to execute
            fetch_one (bool, optional): Whether to return one or all results. Defaults to False.

        Returns:
            [list]: List of results
        """
        connection = self.create_connection(self.db)
        with connection as db:
            # Add dictionary flag so results are retured in key value pairs
            cursor = db.cursor(dictionary=True)
            cursor.execute(query)
            # Check if need to only fetch one
            if fetch_one:
                query_result = cursor.fetchone()
            else:
                query_result = cursor.fetchall()

        return query_result
    # Will need to make one for updating
    # Will need to make one for creating new exercises