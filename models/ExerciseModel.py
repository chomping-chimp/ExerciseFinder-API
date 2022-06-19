from .helpers.EnumClasses import Filters
from .BaseModel import BaseModel

class ExerciseModel(BaseModel):

    def __init__(self):
        super(BaseModel, self).__init__()

    def create_new_exercise(self):
        # TODO: Create POST endpoint to handle individual exercise creation
        pass
    
    def get_all_exercises(self):
        result = self.fetch_all("SELECT * FROM Fitness.Exercises")
        status = 200
        return result, status
    
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
            result = self.fetch_all("SELECT * from Fitness.Exercises WHERE %s", tuple(search_terms))
            status = 200
            return result, status
        except:
            status = 404
            return None, status

    def get_exercise_by_name(self, name, strict=False):
        
        if eval(strict):
            query = "SELECT * FROM Fitness.Exercises WHERE exerciseName = '%s'"%name
        else:
            query = f"SELECT * FROM Fitness.Exercises WHERE exerciseName LIKE '%{name}%'"

        result = self.fetch_all(query)
        status = 200
        return result, status
