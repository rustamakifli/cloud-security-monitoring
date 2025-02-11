from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

db_uri = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER_USED')}:{os.getenv('MYSQL_ROOT_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'top-secret!'

from app.config import *
from app.models import *

if __name__ == '__main__':
    app.init_app(db)
    # login_manager.init_app(app)
    app.init_app(migrate)
    app.run(port=5000, debug=True)