from flask import Flask
from .database import db
from .config import Config
from .routes import routes


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile("config.py", silent=True)

    db.init_app(app)
    app.register_blueprint(routes)

    return app
