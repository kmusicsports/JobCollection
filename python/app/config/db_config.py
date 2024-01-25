import os

SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]
SECRET_KEY = os.urandom(24)
