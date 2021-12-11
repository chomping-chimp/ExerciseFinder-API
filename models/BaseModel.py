from adapters.db import DB

class BaseModel:

    def __init__(self):
        pass
    
    def db(self, dictionary=False):
        return DB()