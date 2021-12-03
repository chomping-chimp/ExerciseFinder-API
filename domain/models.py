from adapters import db
from enum import Enum

class Exercise:
    
    def __init__(self):
        self.db = db.DB()
        self.Filters = Enum('Filters', 'category difficulty equipment exerciseName family primaryTargets subFamily')

    def create_new_exercise(self):
        pass
    
    def get_all_exercises(self):
        query = "SELECT * FROM Fitness.Exercises"
        result = self.db.db_get(query)
        return result
    
    def get_exercise_by_filter(self, filter_term):
        is_valid_filter = False
        for filters in self.Filters:
            if filter_term != filters.name:
                continue
            else:
                is_valid_filter = True
                break
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
