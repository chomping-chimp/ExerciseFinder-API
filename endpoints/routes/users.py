from endpoints.config import settings
from endpoints.helpers import RequestHelper
from flask import Blueprint, render_template

user = Blueprint('user', __name__)
response = RequestHelper()

variables = {
	"email": settings.contact_email,
	"footer_text": "Exercise API | Workout Log"
}

'''
Home page
'''
@user.route('/')
@user.route('/home')
def index():
    variables['title'] = 'Workout Log'
    return render_template('home.html', config=variables)

