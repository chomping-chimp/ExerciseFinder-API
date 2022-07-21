import requests
import os.path
import logging
from dotenv import load_dotenv

logging.basicConfig(level = logging.INFO)

class DataLoad(object):

    def __init__(self): 
        load_dotenv()
        self.SHEET_URL = os.environ.get('SHEET_URL')
        self.logger = logging.getLogger("dataloader")

    def load(self):
        """
        Load data from Sheets
        """
        # Consider creating new auth method to handle username and pass for authentication
        raw_data = requests.get(self.SHEET_URL)

        if not raw_data:
            empty_message = "No data received from Sheets"
            self.logger.warning(empty_message)
        else:
            self.logger.info("Received new data from Sheets")

        return raw_data.text
    
    def process(self):
        
        raw_data = self.load()
        # need to get configs from import_configurations table 
        # in DB and check if data is clean

    def execute(self):
        pass

