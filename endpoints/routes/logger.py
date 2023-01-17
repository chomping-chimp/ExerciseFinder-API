from endpoints.config import settings
from lib.models.UserLogModel import UserLogModel
from endpoints.helpers import RequestHelper
from flask import Blueprint, render_template

logger = Blueprint('logger', __name__)
response = RequestHelper()

variables = {
	"email": settings.contact_email,
	"footer_text": "Exercise API | Workout Log"
}

'''
Public Endpoints for Logger section
'''
@logger.route('/')
@logger.route('/home')
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

