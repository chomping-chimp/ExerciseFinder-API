
import sys
from mysqlx import IntegrityError
from endpoints.helpers import RequestHelper
from .BaseModel import BaseModel

class UserModel(BaseModel):

    def __init__(self, username=None):
        super().__init__()
        self.username = username
        self.is_created = True if username else False

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
