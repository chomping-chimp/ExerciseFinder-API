from bottle import request, response
from bottle import post, get, put, delete
from bottle import Bottle, run
import json
from api import fetcher

app = Bottle()

@app.route('/api/allExercise')
def fetch():
    data = fetcher.get_all()
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'
    return json.dumps({'data': data})

# @put('/names/<name>')
# def update_handler(name):
#     '''Handles name updates'''
#     pass

# @delete('/names/<name>')
# def delete_handler(name):
#     '''Handles name deletions'''
#     pass

# @post('/names')
# def creation_handler():
#     '''Handles name creation'''
#     pass

run(app, host='localhost', port=8080, fast=True)