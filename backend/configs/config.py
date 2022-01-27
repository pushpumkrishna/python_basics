import configparser
import multiprocessing
import os
from typing import Dict, Any, List
from flask import app as flask_app
from utils.constants import DEV

config = configparser.RawConfigParser()
config.read("{}/{}".format(os.path.join(os.path.dirname(__file__)), "config.ini"))
ENV = os.environ.get("FLASK_ENV", DEV)


class Config:
    SECRET_KEY: str
    ENV: str
    DEBUG: str
    WORKERS: int
    HOST: str
    PORT: str
    LOGGING_TYPE: str
    AIML_MONGODB_URI: str
    PORTAL_MONGODB_URI: str
    LOG_PATH: str

    def load_config(self):
        self.SECRET_KEY = os.getenv("SECRET_KEY", config.get(ENV, "secret_key", fallback=""))
        self.ENV = os.getenv("ENV", config.get(ENV, "env", fallback="dev"))
        self.DEBUG = os.getenv("DEBUG", config.getboolean(ENV, "debug", fallback="false"))
        self.WORKERS = os.getenv("WORKERS", multiprocessing.cpu_count() * 2 + 1)
        self.HOST = os.getenv("HOST", config.get(ENV, "host", fallback="0.0.0.0"))
        self.PORT = os.getenv("PORT", config.getint(ENV, "port", fallback="5002"))
        self.LOGGING_TYPE = os.getenv("LOGGING_TYPE", config.get(ENV, "logging_type", fallback="ERROR"))
        self.AIML_MONGODB_URI = os.getenv("AIML_MONGODB_URI", config.get(ENV, "aiml_mongodb_uri", fallback=""))
        self.PORTAL_MONGODB_URI = os.getenv("PORTAL_MONGODB_URI", config.get(ENV, "portal_mongodb_uri", fallback=""))
        self.LOG_PATH = os.getenv("LOG_PATH", config.get(ENV, "log_path", fallback=""))

    def get_config(self) -> Dict[str, Any]:
        """Get config and turn it into dictionary
        :return: dictionary object
        """
        return self.__dict__

    @staticmethod
    def read_config(

    ):
        """Load config from class it self
        :return: config class
        """
        c = Config()
        c.load_config()
        return c


def config_from_ini(app: flask_app):
    """Append configuration from ini file to flask config
    :param app: flask config object
    :return: None
    """
    cfg = Config()
    cfg.load_config()
    app.config.from_object(cfg)
