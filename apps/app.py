from flask import Flask
import os
from dotenv import load_dotenv
from apps.config import db, migrate, login_manager

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

db_uri = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER_USED')}:{os.getenv('MYSQL_ROOT_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'top-secret!'
app.config['STATIC_FOLDER'] = 'static'

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)