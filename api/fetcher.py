from . import db_api
import json
db = db_api.DB()

def get_all():
    result = db.db_get("select * from Fitness.exerciseList")
    print(result)
    return result