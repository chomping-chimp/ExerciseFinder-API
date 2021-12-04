import json
from models.ExerciseModel import ExerciseModel
from endpoints.helpers import RequestHelper
from flask import Flask, request, make_response, Blueprint

exercise = Blueprint('exercise', __name__)
response = RequestHelper()

'''
Index/Home of Application
'''
@exercise.route('/')
@exercise.route('/home')
def index():
    # Work on returning a static page with a guide on the endpoints and features
    return "<h1>Welcome to our server !!</h1>"

'''
Route to get all exercises 
'''
@exercise.route('/exercise/getAll', methods=['GET'])
def respond():
    # Initialize model. Might need to make this outside of function
    exercise_model = ExerciseModel()
    # Create response
    resp = make_response({'data': exercise_model.get_all_exercises()})
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp

'''
Route to filter through exercises based on Muscle Group
WORK IN PROGRESS ------
'''
@exercise.route('/exercise/filter', methods=['GET'])
def filterData():
    filters = request.args.get('filters', '')
    resp = make_response({'data': filters})
    resp = response.create_request_headers(resp)
    #resp['data'] = json.dumps(fetcher.get_all())
    #resp = make_response(json.dumps({'data': fetcher.filterGroups(filters)}))
    return resp
