import json
from endpoints.helpers import RequestHelper
from .UserModel import UserModel

class UserTemplateModel(UserModel):
    
    def __init__(self, user_id=None):
        super(UserModel, self).__init__()
        self.user_id = user_id

    def get_user_template(self, template_id=None):
        
        where = "WHERE user_id = %(user_id)s"
        params = {'user_id': self.user_id}
        if template_id:
            where += " AND template_id = %(template_id)s"
            params['template_id'] = template_id
        
        with self.db('dict') as cursor:
            cursor.execute(f"SELECT * from user_template {where}", params=params)
            result = cursor.fetchall()

        return result

    def create_new_template(self, raw_template):

        template = self.process_raw_template(raw_template)
        
        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO user_template (name,user_id,notes,template,date_created) 
                VALUES (%s, %s, %s, %s, NOW())
            """, (template['title'], self.user_id, template['notes'], json.dumps(template['template'])))
        
        return template
    
    def process_raw_template(self, raw_template):
        tidy_template = {
            'title': raw_template['title'][0],
            'date': raw_template['date'][0],
            'notes': raw_template['notes'][0],
            'template': []
        }

        raw_template['exercise'].pop(0)
        counter = 1

        for index, exercise in enumerate(raw_template['exercise'], start=1):
            exercise_dict = {
                'name': exercise,
                'sets': []
            }
            sets = int(raw_template['sets'][index])

            for x in range(sets):
                # print(f"exercise - {exercise} set - {counter}")
                exercise_dict['sets'].append({
                    'label': raw_template['quantLabel'][counter],
                    'quantity': raw_template['quantity'][counter],
                    'pct_1rm': raw_template['pct_1rm'][counter],
                    'rpe': raw_template['rpe'][counter],
                    'rest': raw_template['rest'][counter]
                })

                counter += 1

            tidy_template['template'].append(exercise_dict)
        return tidy_template

    @classmethod
    def convert_json(cls, json_data):
        return json.loads(json_data)
