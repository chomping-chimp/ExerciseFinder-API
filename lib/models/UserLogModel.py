from endpoints.helpers import RequestHelper
from .BaseModel import BaseModel

class UserLogModel(BaseModel):
    
    def __init__(self, user_id=None):
        super(BaseModel, self).__init__()
        self.user_id = user_id
        self.username = self._get_username_from_id(user_id)

    def get_temp_scoreboard(self):

        result = self.fetch_all("""
        SELECT SUM(log.active_minutes) activity, usr.username, DATE(create_time) date
        FROM scoreboard_log log
        JOIN scoreboard_users usr ON usr.id = log.user_id
        GROUP BY usr.username, DAY(create_time)""")
        user_list = []
        for dic in result:
            dic['activity'] = RequestHelper.default_json(dic['activity'])
            if dic['username'] not in user_list:
                user_list.append(dic['username'])

        meta = {
            'count': len(result),
            'num_users': len(user_list)
        }
        return result, meta

    def get_user_logs(self):
        pass

    def create_new_log(self):
        pass

    def _get_username_from_id(self):
        pass
    
