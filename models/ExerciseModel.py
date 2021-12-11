
from .helpers.EnumClasses import Filters
from .BaseModel import BaseModel

class ExerciseModel(BaseModel):

    def create_new_exercise(self):
        pass
    
    def get_all_exercises(self):
        query = "SELECT * FROM Fitness.Exercises"
        result = None

        with self.db() as connection:
            cursor = connection.cursor()
            cursor.execute(query)

            result = cursor.fetchall()
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
    
    def get_exercise_by_name(self, name, strict=False):
        result = None

        if strict:
            query = "SELECT * FROM Fitness.Exercises WHERE exerciseName = '%s'" %name
        else:
            query = f"SELECT * FROM Fitness.Exercises WHERE exerciseName LIKE '%{name}%'"

        with self.db() as connection:
            cursor = connection.cursor()
            cursor.execute(query)

            result = cursor.fetchall()
            return result
