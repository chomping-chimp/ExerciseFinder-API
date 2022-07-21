import json
import sys
from lib.DataLoad import DataLoad
from endpoints.helpers import RequestHelper
from flask import request, make_response, Blueprint

dataload = Blueprint('dataload', __name__)
response = RequestHelper()

@dataload.route('/dataload/run', methods=['GET'])
def run_dataload():
    loader = DataLoad()
    return loader.load()
