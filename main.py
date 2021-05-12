import json
from flask import Flask, request, jsonify, make_response
from flask import Response
from api import fetcher

app = Flask(__name__)

@app.route('/exercise/getAll', methods=['GET'])
def respond():
    resp = make_response(json.dumps({'data': fetcher.get_all()}))
    resp.headers['Content-Type'] = 'application/json'
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Credentials'] = 'GET, POST, OPTIONS'
    resp.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'
    return resp

# @app.route('/exercise/getAll', methods=['GET'])
# def respond():
#     resp = make_response(json.dumps({'data': fetcher.get_all()}))
#     resp.headers['Content-Type'] = 'application/json'
#     resp.headers['Access-Control-Allow-Origin'] = '*'
#     resp.headers['Access-Control-Allow-Credentials'] = 'GET, POST, OPTIONS'
#     resp.headers['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'
#     return resp
# Need to look into 

# @app.route('/post/', methods=['POST'])
# def post_something():
#     param = request.form.get('name')
#     print(param)
#     # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
#     if param:
#         return jsonify({
#             "Message": f"Welcome {name} to our awesome platform!!",
#             # Add this option to distinct the POST request
#             "METHOD" : "POST"
#         })
#     else:
#         return jsonify({
#             "ERROR": "no name found, please send a name."
#         })

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)