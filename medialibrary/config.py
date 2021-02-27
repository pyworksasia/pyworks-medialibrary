import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):

    def __init__(self):
        self.AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
        self.AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

config = Config()
print(config.__dict__)

