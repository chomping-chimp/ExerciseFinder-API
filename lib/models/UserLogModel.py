import json
import re
from endpoints.helpers import RequestHelper
from .UserModel import UserModel

class UserLogModel(UserModel):
    
    def __init__(self, user_id=None):
        super(UserModel, self).__init__()
        self.user_id = user_id

    def get_user_logs(self, workout_id=None):
        where = "WHERE user_id = %(user_id)s"
        params = {'user_id': self.user_id}
        if workout_id:
            where += " AND workout_id = %(workout_id)s"
            params['workout_id'] = workout_id
        
        with self.db('dict') as cursor:
            cursor.execute(f"SELECT * from workout_log {where}", params=params)
            result = cursor.fetchall()

        return result

    def create_new_log(self, template):
        
        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO workout_log (user_id,details,date) 
                VALUES (%s, %s, NOW())
            """, (self.user_id, json.dumps(template)))

    def add_load_to_template(self, template, count_list, load_list):

        counter = 0
        template = json.loads(template)

        for exercise in template:
            for work_set in exercise['sets']:

                work_set['count'] = count_list[counter]
                work_set['load'] = load_list[counter]
                counter += 1

        return template
    
    def extract_from_text(self, raw_text):
        # pattern = r"#\s*\w[\w\s]*"
        # exercises = re.findall(pattern, raw_text)
        # print(exercises)

        # pattern = r"\[(.*?)\]"
        # rep_scheme = re.findall(pattern, raw_text)
        # print(rep_scheme)

        # pattern = r"[0-9]{1,3}x[0-9]{1,3}\\"
        # rep_scheme = re.findall(pattern, raw_text)
        # print(rep_scheme)
        exercises = raw_text.split('#')
        exercises.remove(exercises[0])
        exercise_list = []
        for x in exercises:
            x = x.replace("\r\n", '\n')
            print(x)
            exercise = x.split('\n')
            exercise_list.append({
                'name': exercise[0],
                'rep_scheme': exercise[1],
                'sets': exercise[2:]
            })
        return exercise_list
