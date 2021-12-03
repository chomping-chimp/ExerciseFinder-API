import json
from domain.models import Exercise
from endpoints.helpers import RequestHelper
from flask import Flask, request, make_response, Blueprint

routes = Blueprint('routes', __name__)
response = RequestHelper()

'''
Index/Home of Application
'''
@routes.route('/')
@routes.route('/home')
def index():
    # Work on returning a static page with a guide on the endpoints and features
    return "<h1>Welcome to our server !!</h1>"

'''
Route to get all exercises 
'''
@routes.route('/exercise/getAll', methods=['GET'])
def respond():
    # Initialize model. Might need to make this outside of function
    exercise_model = Exercise()
    # Create response
    resp = make_response({'data': exercise_model.get_all_exercises()})
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp

'''
Route to filter through exercises based on Muscle Group
WORK IN PROGRESS ------
'''
@routes.route('/exercise/filter', methods=['GET'])
def filterData():
    filters = request.args.get('filters', '')
    resp = response.create_request_headers()
    #resp['data'] = json.dumps(fetcher.get_all())
    #resp = make_response(json.dumps({'data': fetcher.filterGroups(filters)}))
    return resp
