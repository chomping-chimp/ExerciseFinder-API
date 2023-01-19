from endpoints.config import settings
from lib.models.UserLogModel import UserLogModel
from endpoints.helpers import RequestHelper
from flask import Blueprint, render_template, request, redirect, url_for

from lib.models.UserModel import UserModel

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

@logger.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        is_auth = UserModel().authenticate_user(user, password)
        if is_auth:
            return redirect(url_for('.dashboard'))
        else:
            return redirect(url_for('.login', name=user))
    else:
        variables['title'] = 'Login'
        return render_template('login.html', config=variables)

@logger.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        email = request.form['email']
        create_user = UserModel().create_new_user(user, password, email)
        if create_user:
            return redirect(url_for('.login', name=user))
        else:
            return redirect(url_for('.signup', name=user))
    else:
        variables['title'] = 'Sign Up'
        return render_template('signup.html', config=variables)

'''
Private Endpoints for logger section
'''
@logger.route('/dashboard')
def dashboard():
    variables['title'] = 'Workout Log'
    return render_template('dashboard.html', config=variables)

@logger.route('/logout')
def logout():
    variables['title'] = 'Login'
    return render_template('login.html', config=variables)

