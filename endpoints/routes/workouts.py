from endpoints.config import settings
from lib.models.UserLogModel import UserLogModel
from endpoints.helpers import RequestHelper
from flask import Blueprint, render_template, request, redirect, url_for

from lib.models.UserModel import UserModel

workout = Blueprint('workout', __name__)
response = RequestHelper()

variables = {
	"email": settings.contact_email,
	"footer_text": "Exercise API | Workout Log",
    "cache": settings.CACHE_VERSION
}

@workout.route('/template/create-new', methods=['POST', 'GET'])
def create_new():
    variables['title'] = 'Create New'
    return render_template('edit_workout.html', config=variables)

@workout.route('/login', methods=['POST', 'GET'])
def passd():
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


