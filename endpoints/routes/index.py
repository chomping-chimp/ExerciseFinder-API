from lib.models.ExerciseModel import ExerciseModel
from endpoints.helpers import RequestHelper
from flask import request, make_response, Blueprint, render_template

index = Blueprint('index', __name__)
response = RequestHelper()

'''
Index/Home of Application
'''
@index.route('/')
@index.route('/home')
def home():
    return render_template('index.html', title='Exercise API')

@index.route('/form')
def form():
    return render_template('form.html', title='New Exercise')

# Need func for getting all exercises in template
# Need func for getting one exercise in template
# Need func for filtering - Maybe make JS call to /api?
# Need func for creating a new exercise
