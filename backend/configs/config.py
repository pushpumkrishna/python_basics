import configparser
import multiprocessing
import os
from typing import Dict, Any, List
from flask import app as flask_app
from utils.constants import DEV

config = configparser.RawConfigParser()
config.read("{}/{}".format(os.path.join(os.path.dirname(__file__)), "config.ini"))
ENV = os.environ.get("FLASK_ENV", "lo")
print(ENV)
print(config.get("local_env", "le lo"))
