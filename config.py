import os
from dotenv import load_dotenv

load_dotenv()

IS_DEBUG = os.getenv('DEBUG_MODE', 'False').lower() in ('true', '1', 't')

class BaseConfig:
    @property
    def track_url(self):
        "url сервера"
        return 'http://127.0.0.1:5001' if IS_DEBUG else os.getenv('SERVER_URL')

class ConfigMaker(BaseConfig):
    IS_DEBUG = IS_DEBUG

    class Flask:
        SESSION_KEY = os.getenv('FLASK_SESSION_KEY')
        URL = f'{BaseConfig().track_url}'

Config = ConfigMaker()