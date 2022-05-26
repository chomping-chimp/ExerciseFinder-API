import json
import sys
from models.UserModel import UserModel
from models.GroupModel import GroupModel
from endpoints.helpers import RequestHelper
from flask import request, jsonify, make_response, Blueprint

activity = Blueprint('activity', __name__)
response = RequestHelper()

'''
Get User Data from username
'''
@activity.route('/activity/user/<username>', methods=['GET'])
def getUser(username):
    user_data = UserModel(username).get_user()
    resp = make_response({'data': user_data})
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp

'''
Register new user
'''
@activity.route('/activity/user/create', methods=['POST'])
def createUser():
    data = request.get_json(force=True)
    username = data.get('username')
    result, status = UserModel().create_new_user(username)
    resp = make_response({'data': result, 'status': status})
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp

'''
Log activity
'''
@activity.route('/activity/user/<username>/log-activity', methods=['POST'])
def logActivity(username):
    # Get data from headers
    data = request.get_json()
    minutes = data.get('minutes')
    # Pass in and get result
    result = UserModel(username).record_activity(minutes)
    # Form response
    op_status = 'OK' if result == 200 else 'FAIL'
    resp = make_response({'status': op_status, 'code': result})
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp

'''
Get user stats
'''
@activity.route('/activity/user/<username>/stats', methods=['GET'])
def userStats(username):

    user_data = UserModel(username).get_user_stats()
    resp = make_response({'data': user_data, 'user': username})
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp

'''
Get Scoreboard - TEMP ENDPOINT see below
'''
@activity.route('/activity/scoreboard', methods=['GET'])
def getScoreboard():

    timeframe = request.args.get('timeframe', '')
    group_model = GroupModel()
    data, meta = group_model.get_temp_scoreboard(timeframe)
    resp = make_response({'data': data, 'metadata': meta})
    # Add response headers
    resp = response.create_request_headers(resp)
    return resp


# TODO: Create endpoints for groups
# NOTE: Once created, users will only be able to see the scoreboard for the group they are in
# Will have to create a method to construct the scoreboard for each group

'''
Create new group
'''
@activity.route('/activity/group/create', methods=['POST'])
def createGroup():
    return {}

'''
Add user to group
'''
@activity.route('/activity/group/<group_name>/add', methods=['POST'])
def addUser(group_name):
    return {}

'''
Remove user from group
'''
@activity.route('/activity/group/<group_name>/remove', methods=['POST'])
def dropUser(group_name):
    return {}

'''
Get group scoreboard
'''
@activity.route('/activity/group/<group_name>/scoreboard', methods=['GET'])
def getGroupScoreboard(group_name):
    return {}

'''
Delete group
'''
@activity.route('/activity/group/<group_name>/delete', methods=['DELETE'])
def dropGroup(group_name):
    return {}
