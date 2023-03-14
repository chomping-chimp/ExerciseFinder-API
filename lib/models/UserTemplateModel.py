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
            where += " AND t.template_id = %(template_id)s"
            params['template_id'] = template_id
        
        with self.db('dict') as cursor:
            cursor.execute(f"""
                SELECT t.* FROM templates t
                JOIN user_template_map utm ON utm.template_id = t.template_id
                {where}
            """, params=params)
            result = cursor.fetchall()
        return result

    def create_new_template(self, raw_template):

        template = self.process_raw_template(raw_template)
        
        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO templates (name,notes,template,date_created) 
                VALUES (%s, %s, %s, NOW())
            """, (template['title'], template['notes'], json.dumps(template['template'])))
            cursor.execute("SELECT MAX(template_id) AS template_id FROM templates")
            return cursor.fetchone()[0]
        
    def update_template(self, template_id, raw_template):
        template = self.process_raw_template(raw_template)
        
        with self.db() as cursor:
            cursor.execute("""
                UPDATE templates
                SET name=%s, notes=%s, template=%s
                WHERE template_id=%s
            """, (template['title'], template['notes'], json.dumps(template['template']), template_id))
            return template_id
    
    def link_user_to_template(self, template_id):
        
        with self.db() as cursor:
            cursor.execute("""
                INSERT INTO user_template_map (template_id,user_id) 
                VALUES (%s, %s)
            """, (template_id, self.user_id))
    
    def process_raw_template(self, raw_template):
        tidy_template = {
            'title': raw_template['title'][0],
            'notes': raw_template['notes'][0],
            'template': raw_template['template'][0]
        }
        # TODO: better process it here w regex
        return tidy_template

    @classmethod
    def convert_json(cls, json_data):
        if isinstance(json_data, str):
            return json.loads(json_data)
        else:
            return json.dumps(json_data)
