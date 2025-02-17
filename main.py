from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='apps/templates',static_folder='apps/static')

db_uri = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER_USED')}:{os.getenv('MYSQL_ROOT_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'top-secret!'
app.config['STATIC_FOLDER'] = 'static'


from apps.config import *
from apps.models import *
from apps.routes import *

if __name__ == '__main__':
    # db.init_app(app)
    # db.init_app(migrate)
    app.run(port=5000, debug=True)