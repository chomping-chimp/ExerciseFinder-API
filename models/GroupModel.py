from endpoints.helpers import RequestHelper
from models.BaseModel import BaseModel

class GroupModel(BaseModel):
    
    def __init__(self, username=None, group_name=None):
        super(BaseModel, self).__init__()
        self.username = username
        # Likely need to init UserModel eventually
        self.group_name = group_name
        self.is_created = True if group_name else False

    @classmethod
    def create_group(cls, username, group_name):
        pass

    def add_user(self):
        pass
    
    def kick_user(self):
        pass

    def get_scoreboard(self, timeframe=None):
        
        query = ""
        if timeframe == "day":
            query = """
                SELECT usr.username, SUM(log.active_minutes) activity, log.create_time date
                FROM scoreboard_log log
                JOIN scoreboard_users usr ON usr.id = log.user_id
                WHERE log.create_time <= NOW() AND log.create_time >= NOW() - INTERVAL 12 hour
                GROUP BY DAY(create_time), usr.username;
            """
        elif timeframe == "week":
            query = """
                SELECT usr.username, SUM(log.active_minutes) activity, log.create_time date
                FROM scoreboard_log log
                JOIN scoreboard_users usr ON usr.id = log.user_id
                WHERE log.create_time <= NOW() AND log.create_time >= NOW() - INTERVAL 7 day
                GROUP BY DAY(create_time), usr.username;
            """
        else:
            query = """
                SELECT usr.username, SUM(log.active_minutes) activity, MAX(log.create_time) date
                FROM scoreboard_log log
                JOIN scoreboard_users usr ON usr.id = log.user_id
                GROUP by usr.username;
            """

        result = self.fetch_all(query)
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

    def delete_group(self):
        pass

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
