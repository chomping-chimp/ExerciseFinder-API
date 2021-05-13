import json
from flask import Flask, request, jsonify, make_response
from flask import Response
from api import fetcher

app = Flask(__name__)

'''
Testing Route to check server
'''
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

'''
Route to get all exercises 
'''
@app.route('/exercise/getAll', methods=['GET'])
def respond():
    resp = make_response(json.dumps({'data': fetcher.get_all()}))
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Credentials'] = 'GET, POST, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'
    return resp

'''
Route to filter through exercises based on Muscle Group
'''
@app.route('/exercise/filter', methods=['GET'])
def filterData():
    filters = request.args.get('filters', '')
    resp = make_response(json.dumps({'data': fetcher.filterGroups(filters)}))
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Credentials'] = 'GET, POST, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'
    return resp

# http://127.0.0.1:5000/exercise/filter?filters=name%impo

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)