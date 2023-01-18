from endpoints.helpers import RequestHelper
from .BaseModel import BaseModel

class UserLogModel(BaseModel):
    
    def __init__(self, user_id=None):
        super(BaseModel, self).__init__()
        self.user_id = user_id
        self.username = self._get_username_from_id(user_id)

    def get_user_logs(self):
        pass

    def create_new_log(self):
        pass

    def _get_username_from_id(self):
        pass
    
