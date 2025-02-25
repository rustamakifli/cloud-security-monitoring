from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# from main import app as app

# #how it worked
# try:
#     from main import app as app
# except ImportError:
#     from __main__ import app


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
