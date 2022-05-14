
from flask import Flask
from .exercises import exercise
from .activities import activity

app = Flask(__name__)
app.register_blueprint(exercise)
app.register_blueprint(activity)