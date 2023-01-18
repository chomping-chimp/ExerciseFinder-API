from endpoints.config import settings
from lib.models.UserModel import UserModel
from endpoints.helpers import RequestHelper
from flask import request, make_response, Blueprint, render_template

user = Blueprint('user', __name__)
response = RequestHelper()

variables = {
	"email": settings.contact_email,
	"footer_text": "Exercise API | Workout Log"
}

'''
Public Endpoints for Logger section
'''
@user.route('/')
@user.route('/home')
def index():
    variables['title'] = 'Workout Log'
    return render_template('home.html', config=variables)

@logger.route('/login')
def login():
    variables['title'] = 'Login'
    return render_template('login.html', config=variables)

@logger.route('/signup')
def signup():
    variables['title'] = 'Sign Up'
    return render_template('signup.html', config=variables)

'''
Private Endpoints for logger section
'''
@logger.route('/dashboard')
def dashboard():
    variables['title'] = 'Workout Log'
    return render_template('home.html', config=variables)

