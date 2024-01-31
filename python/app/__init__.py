from flask import Flask

from app.database import db
from app.controller.company_controller import company_page
from app.controller.company_info_controller import company_info_page
from app.controller.company_connection_controller import (
    company_connection_page
)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile("config/db_config.py")
    db.init_app(app)

    app.register_blueprint(company_page)
    app.register_blueprint(company_info_page)
    app.register_blueprint(company_connection_page)

    return app
