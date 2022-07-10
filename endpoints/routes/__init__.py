
from flask import Flask
from .exercises import exercise
from .activities import activity
from .index import index

app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(exercise, url_prefix="/api")
app.register_blueprint(activity, url_prefix="/api")
