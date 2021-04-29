from . import db_api

db = db_api.DB()

def get_all():
    result = db.db_get("select * from Fitness.exerciseList")
    print(result)
    response = json.dumps(result)
    return response