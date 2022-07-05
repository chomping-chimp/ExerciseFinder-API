from .helpers.EnumClasses import Filters
from .BaseModel import BaseModel

class ExerciseModel(BaseModel):

    def __init__(self):
        super().__init__()

    def create_new_exercise(self):
        # TODO: Create POST endpoint to handle individual exercise creation
        pass
    
    def get_all_exercises(self):

        with self.db('dict') as cursor:
            cursor.execute("SELECT * FROM Fitness.Exercises")
            result = cursor.fetchall()

        status = 200
        return result, status
    
    def get_exercise_by_filter(self, filter_term):
        search_query = []
        try:
            for key, value in filter_term.items():
                filter_name = Filters.get_member_key(key)
                if filter_name:
                    search_query.append(f"{key} LIKE '%{value}%'")
                else:
                    raise ValueError("Invalid search term provided")
            
        except ValueError as e:
            print(e)
            status = 404
            return None, status

        search_terms = ' AND '.join(search_query)
        with self.db() as cursor:
            cursor.execute(f"SELECT * from Fitness.Exercises WHERE {search_terms}")
            result = cursor.fetchall()

        status = 200
        return result, status

    def get_exercise_by_name(self, name, strict=False):
        
        if eval(strict):
            query = "SELECT * FROM Fitness.Exercises WHERE exerciseName = '%s'"%name
        else:
            query = f"SELECT * FROM Fitness.Exercises WHERE exerciseName LIKE '%{name}%'"

        with self.db() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        status = 200
        return result, status
