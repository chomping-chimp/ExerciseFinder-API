import logging
from adapters.db import Database

logging.basicConfig(level = logging.INFO)

class BaseModel(object):

    def __init__(self):
        self.db_conn = Database()
        self.logger = logging.getLogger("base_logger")
    
    def db(self, cursor=None):
        return self.db_conn.get_connection(cursor)

