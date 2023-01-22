from endpoints.helpers import RequestHelper
from .BaseModel import BaseModel

class GroupModel(BaseModel):
    
    def __init__(self, username=None, group_name=None):
        super(BaseModel, self).__init__()
        self.username = username
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
        
        where_clause = ""
        if timeframe == "day":
            where_clause = "WHERE log.create_time <= NOW() AND log.create_time >= NOW() - INTERVAL 12 hour"
        elif timeframe == "week":
            where_clause = "WHERE log.create_time <= NOW() AND log.create_time >= NOW() - INTERVAL 7 day"
        else:
            pass
        
        with self.db() as cursor:
            cursor.execute(f"""
                SELECT usr.username, SUM(log.active_minutes) activity, MAX(log.create_time) date
                FROM scoreboard_log log
                JOIN scoreboard_users usr ON usr.id = log.user_id
                {where_clause}
                GROUP BY usr.username
                ORDER BY activity DESC
            """)
            result = cursor.fetchall()
            
        user_list = []
        for row in result:
            row['activity'] = RequestHelper.default_json(row['activity'])
            if row['username'] not in user_list:
                user_list.append(row['username'])

        meta = {
            'count': len(result),
            'num_users': len(user_list)
        }
        return result, meta

    def delete_group(self):
        pass
