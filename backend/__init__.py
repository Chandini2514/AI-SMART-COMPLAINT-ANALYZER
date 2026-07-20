import os
from flask import Flask
from .database import db
from .config import Config
from .routes import routes


def create_app():
    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder=frontend_path,
        static_url_path="",
        template_folder=frontend_path,
    )
    app.config.from_object(Config)
    app.config.from_pyfile("config.py", silent=True)

    db.init_app(app)
    app.register_blueprint(routes)

    with app.app_context():
        from .database import ensure_complaint_columns
        ensure_complaint_columns()

    return app
