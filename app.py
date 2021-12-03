from flask import Flask
from endpoints.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000, debug=True)