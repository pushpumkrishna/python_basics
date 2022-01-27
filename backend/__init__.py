from flask import Flask
from backend.configs.config import config_from_ini
from backend.routes.db_access import dbTest


def create_app():
    app = Flask(__name__)

    # load config from config.ini file
    config_from_ini(app)

    # register our blueprints
    app.register_blueprint(dbTest)
    # app.register_blueprint(image_routes)
    # app.register_blueprint(mlc_text_routes)
    # app.register_blueprint(mlc_video_routes)
    # app.register_blueprint(offensive_text_routes)
    # app.register_blueprint(video_routes)
    # app.register_blueprint(publish_unpublish_routes)

    return app
