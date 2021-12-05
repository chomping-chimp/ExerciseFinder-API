
from flask import Flask
from .exercises import exercise

app = Flask(__name__)
app.register_blueprint(exercise)