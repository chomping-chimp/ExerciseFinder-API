from endpoints.helpers import RequestHelper
from .UserModel import UserModel

class UserLogModel(UserModel):
    
    def __init__(self, user_id=None):
        super(UserModel, self).__init__()
        self.user_id = user_id
        self.username = self.get_username(id=user_id)

    def get_user_logs(self):
        pass

    def create_new_log(self):
        pass
