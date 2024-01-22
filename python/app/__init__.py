from flask import Flask

from app.controller.company_controller import company_page
from app.database import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile("config/db_config.py")
    db.init_app(app)

    app.register_blueprint(company_page)

    return app