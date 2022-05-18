
import sys
from mysqlx import IntegrityError
from endpoints.helpers import RequestHelper
from models.BaseModel import BaseModel

class UserModel(BaseModel):

    def __init__(self, username=None):
        super(BaseModel, self).__init__()
        self.username = username
        self.is_created = True if username else False

    def get_user_stats(self):
        # TODO: Create better data output for this part
        # Could split into avg minutes per day/week/month, most active day
        if not self.is_created:
            return 404

        user_id = self.get_user_id()['id']
        data = self.fetch_all("""
        SELECT usr.username, sum(log.active_minutes) total_activity, count(log.id) total_records
        FROM scoreboard_log log
        JOIN scoreboard_users usr ON usr.id = log.user_id AND log.user_id = %s
        """, (user_id,))
        
        for dic in data:
            dic['total_activity'] = RequestHelper.default_json(dic['total_activity'])
            del dic['username']

        return data
    
    def record_activity(self, minutes):
        # If user is not created, exit
        if not self.is_created:
            return 404
        
        try:
            user_id = self.get_user_id()['id']
            # Insert record into table with ID
            print(minutes, file=sys.stderr)
            self.execute("""
                INSERT INTO scoreboard_log (user_id, active_minutes)
                VALUES (%s, %s)""", (user_id, minutes)
            )
            return 200
        except IntegrityError:
            return 500

    def get_user(self):
        # If user is not created, return empty
        if not self.is_created:
            return {}

        result = self.fetch_one("""
            SELECT usr.username, usr.created_datetime, grp.group_name, usr.id
            FROM scoreboard_users usr
            LEFT JOIN scoreboard_groups grp ON grp.id = usr.group_id
            WHERE usr.username = %s
            """, (self.username, ))
        
        # TODO: Can fix some of the data here later?
        return result
        
    def create_new_user(self, username):

        if self.user_exists(username):
            self.is_created = True
            self.username = username
            return {}, 300

        self.execute("INSERT INTO scoreboard_users (username) VALUES (%s)", (username, ))
        self.username = username
        result = self.get_user_id()
        status = 200 if result else 500
        return result, status

    def user_exists(self, username):
        # Check to see if user already exists in the DB
        result = self.fetch_all("SELECT * FROM scoreboard_users WHERE username = %s", (username, ))
        return True if result else False

    def get_user_id(self):
        # Get user id
        user_id = self.fetch_one("SELECT id from scoreboard_users WHERE username = %s", (self.username,))
        return user_id