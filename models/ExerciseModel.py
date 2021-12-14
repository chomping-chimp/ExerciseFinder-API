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
        search_query = []
        try:

            for key, value in filter_term.items():
                filter_name = Filters.get_member_key(key)
                if filter_name:
                    search_query.append(f"({key} = \'{value}\')")
                else:
                    raise Exception("Invalid search term provided")
                
            search_terms = " AND ".join(search_query)
            query = "SELECT * from Fitness.Exercises WHERE %s" %search_terms

            with self.db() as connection:
                cursor = connection.cursor()
                cursor.execute(query)

                result = cursor.fetchall()
                status = 200
                return result, status
        except:
            status = 404
            return None, status

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
