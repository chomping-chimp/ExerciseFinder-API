from adapters import db
from .helpers.EnumClasses import Filters

class ExerciseModel:
    
    def __init__(self):
        self.db = db.DB()

    def create_new_exercise(self):
        pass
    
    def get_all_exercises(self):
        query = "SELECT * FROM Fitness.Exercises"
        result = self.db.db_get(query)
        return result
    
    def get_exercise_by_filter(self, filter_term):
        is_valid_filter = False
        filter = Filters.get_member_key(filter_term)
        #splitList = filterList.split('%')
        # if (len(splitList) == 1):
        #     filters = splitList[0]
        #     query = ("SELECT * FROM Fitness.AllExercises WHERE `Primary Muscle` = '{}'".format(filters))
        # else:
        #     filters = tuple(splitList)
        #     query = ("SELECT * FROM Fitness.AllExercises WHERE `Primary Muscle` IN {}".format(filters))
        # result = db.db_get(connection, query)
        # return result
        pass
    
    def __get_exercise_by_name(self, name, strict=False):
        pass
