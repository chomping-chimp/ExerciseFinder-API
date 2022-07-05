
import sys
from mysqlx import IntegrityError
from endpoints.helpers import RequestHelper
from models.BaseModel import BaseModel

class UserModel(BaseModel):

    def __init__(self, username=None):
        super().__init__()
        self.username = username
        self.is_created = True if username else False

    def get_user_stats(self):
        if not self.is_created:
            return 404

        user_id = self.get_user_id()
        with self.db('dict') as cursor:
            cursor.execute("""
                SELECT usr.username, sum(log.active_minutes) total_activity, count(log.id) total_records
                FROM scoreboard_log log
                JOIN scoreboard_users usr ON usr.id = log.user_id AND log.user_id = %s
            """, (user_id,))
            data = cursor.fetchall()
        
        for row in data:
            row['total_activity'] = RequestHelper.default_json(row['total_activity'])
            del row['username']

        return data
    
    def record_activity(self, minutes):
        # If user is not created, exit
        if not self.is_created:
            return 404
        
        try:
            user_id = self.get_user_id()
            # Insert record into table with ID
            print(minutes, file=sys.stderr)
            with self.db('dict') as cursor:
                cursor.execute("""
                    INSERT INTO scoreboard_log (user_id, active_minutes)
                    VALUES (%s, %s)
                """, (user_id, minutes))
            return 200
        except IntegrityError:
            return 500

    def get_user(self):
        # If user is not created, return empty
        if not self.is_created:
            return {}
        
        with self.db('dict') as cursor:
            cursor.execute("""
                SELECT usr.username, usr.created_datetime, grp.group_name, usr.id
                FROM scoreboard_users usr
                LEFT JOIN scoreboard_groups grp ON grp.id = usr.group_id
                WHERE usr.username = %s
            """, (self.username, ))
            result = cursor.fetchone()
        
        # TODO: Can fix some of the data here later?
        return result
        
    def create_new_user(self, username):

        if self.user_exists(username):
            self.is_created = True
            self.username = username
            return {}, 300

        with self.db('dict') as cursor:
            cursor.execute("INSERT INTO scoreboard_users (username) VALUES (%s)", (username, ))

        self.username = username
        result = self.get_user_id()

        status = 200 if result else 500
        return result, status

    def user_exists(self, username):
        # Check to see if user already exists in the DB
        with self.db('dict') as cursor:
            cursor.execute("SELECT * FROM scoreboard_users WHERE username = %s", (username, ))
            result = cursor.fetchall()

        return True if result else False

    def get_user_id(self):
        # Get user id
        with self.db('dict') as cursor:
            cursor.execute("SELECT id from scoreboard_users WHERE username = %s", (self.username,))
            result = cursor.fetchone()
        
        return result['id']
