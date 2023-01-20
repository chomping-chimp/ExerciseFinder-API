from flask import Flask

from .exercises import exercise
from .activities import activity
from .workouts import workout
from .logger import log
from .index import index

app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(exercise, url_prefix="/api")
app.register_blueprint(activity, url_prefix="/api")

app.register_blueprint(log, url_prefix="/log")
app.register_blueprint(workout, url_prefix="/log")
