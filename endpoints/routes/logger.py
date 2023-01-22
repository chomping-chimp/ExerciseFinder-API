from endpoints.config import settings
from endpoints.helpers import RequestHelper
from flask import Blueprint, render_template, request, session, redirect, url_for

from lib.models.UserModel import UserModel
from lib.models.UserTemplateModel import UserTemplateModel

log = Blueprint('log', __name__)
response = RequestHelper()

variables = {
	"email": settings.contact_email,
	"footer_text": "Exercise API | Workout Log",
    "cache": settings.CACHE_VERSION,
}

'''
Public Endpoints for Logger section
'''
@log.route('/')
@log.route('/home')
def index():
    variables['title'] = 'Workout Log'
    return render_template('home.html', config=variables)

@log.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_model = UserModel()

        user = request.form['username']
        password = request.form['password']
        # check if user is authenticated
        is_auth = user_model.authenticate_user(user, password)
        if is_auth:
            # Get user_id
            user_id = user_model.get_user_id(username=user)
            # set to session
            session['user_id'] = user_id
            session['username'] = user
            return redirect(url_for('log.dashboard', user_id=user_id))
        else:
            return redirect(url_for('log.login', name=user))
    else:
        # implement a user session system?
        variables['title'] = 'Login'
        return render_template('login.html', config=variables)

@log.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        email = request.form['email']
        create_user = UserModel().create_new_user(user, password, email)
        if create_user:
            return redirect(url_for('log.login', name=user))
        else:
            return redirect(url_for('log.signup', name=user))
    else:
        variables['title'] = 'Sign Up'
        return render_template('signup.html', config=variables)

'''
Private Endpoints for logger section
'''
@log.route('/dashboard')
def dashboard():
    variables['title'] = 'Workout Log'
    # Use UserTemplateModel for this
    variables['templates'] = []
    templates = UserTemplateModel(session.get('user_id')).get_user_template()
    for template in templates:
        variables['templates'].append({
            'name': template['name'],
            'id': template['template_id']
        })
    # UserLogModel for this
    variables['history'] = [
        {
            'template': 'Upper Strength',
            'date': '2023-01-19'
        },
        {
            'template': 'Lower Strength',
            'date': '2023-01-17'
        },
        {
            'template': 'Full Body',
            'date': '2023-01-16'
        },
    ]
    return render_template('dashboard.html', config=variables)

@log.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect(url_for('log.login'))

