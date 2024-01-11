from flask import Flask
from controller.company_controller import company_page

app = Flask(__name__)
app.register_blueprint(company_page)
