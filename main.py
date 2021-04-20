from bottle import request, response
from bottle import post, get, put, delete
from bottle import Bottle, run
import api.db_api as sql

app = Bottle()
db = sql.DB()

@app.route('/api/exercise')
def hello():
    result = db.db_get()
    print(result)
    return result

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