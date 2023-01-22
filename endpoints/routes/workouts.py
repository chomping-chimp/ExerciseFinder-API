from endpoints.config import settings
from lib.models.UserTemplateModel import UserTemplateModel
from endpoints.helpers import RequestHelper
from flask import Blueprint, render_template, session, request, redirect, url_for

workout = Blueprint('workout', __name__)
response = RequestHelper()

variables = {
	"email": settings.contact_email,
	"footer_text": "Exercise API | Workout Log",
    "cache": settings.CACHE_VERSION
}

@workout.route('/template/create-new', methods=['POST', 'GET'])
def create_new():
    if request.method == 'POST':
        user_id = session.get('user_id')
        d = request.form.to_dict(flat=False)
        UserTemplateModel(user_id).create_new_template(d)
        return redirect(url_for('log.dashboard', user_id=user_id))
    else:
        variables['title'] = 'Create New'
        return render_template('new_workout.html', config=variables)

@workout.route('template/<template_id>/edit', methods=['POST', 'GET'])
def edit_template(template_id):
    if request.method == 'POST':
        pass
    else:
        user_id = session.get('user_id')
        template = UserTemplateModel(user_id).get_user_template(template_id)

        variables['workout'] = template[0]
        variables['workout']['template'] = UserTemplateModel.convert_json(variables['workout']['template'])

        return render_template('edit_template.html', config=variables)

@workout.route('template/<template_id>/log', methods=['POST', 'GET'])
def log_workout(template_id):
    if request.method == 'POST':
        d = request.form.to_dict(flat=False)
        # Use new model to get template from template ID
        # then add the sets and reps to the existing data based on indexing
        print(d)
        return redirect(url_for('log.dashboard'))
    else:
        user_id = session.get('user_id')
        template = UserTemplateModel(user_id).get_user_template(template_id)

        variables['template_id'] = template_id
        variables['workout'] = template[0]
        variables['workout']['template'] = UserTemplateModel.convert_json(variables['workout']['template'])

        return render_template('log_workout.html', config=variables)
