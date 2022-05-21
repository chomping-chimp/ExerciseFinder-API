from models.ExerciseModel import ExerciseModel
from endpoints.helpers import RequestHelper
from flask import request, make_response, Blueprint, render_template

exercise = Blueprint('exercise', __name__)
response = RequestHelper()

'''
Index/Home of Application
'''
@exercise.route('/')
@exercise.route('/home')
def index():
    return render_template('index.html', title='Exercise API')

'''
Route to get all exercises 
'''
@exercise.route('/exercise/get-all', methods=['GET'])
def get_all_exercises():

    exercise_model = ExerciseModel()
    exercises, status = exercise_model.get_all_exercises()
    metadata = response.create_response_meta(exercises, status)

    resp = make_response(
        {
            'data': exercises,
            'metadata': metadata
        }
    )
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp

@exercise.route('/exercise/get-one', methods=['GET'])
def get_one_exercise():

    name = request.args.get('name', '')
    exact = eval(request.args.get('exact', ''))

    exercise_model = ExerciseModel()
    exercises, status = exercise_model.get_exercise_by_name(name, strict=exact)
    metadata = response.create_response_meta(exercises, status)

    resp = make_response(
        {
            'metadata': metadata,
            'data': exercises
        }
    )
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp

'''
Route to filter through exercises based on Muscle Group
WORK IN PROGRESS ------
'''
@exercise.route('/exercise/filter', methods=['GET'])
def filter_exercises():
    filters = request.args

    exercise_model = ExerciseModel()
    exercises, status = exercise_model.get_exercise_by_filter(filter_term=filters)
    metadata = response.create_response_meta(exercises, status)

    resp = make_response(
        {
            'metadata': metadata,
            'data': exercises
        }
    )
    resp = response.create_request_headers(resp)
    return resp
