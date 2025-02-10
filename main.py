from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@db:3306/cloud_security'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'top-secret!'

from app.config import *
from app.models import *

if __name__ == '__main__':
    app.init_app(db)
    # login_manager.init_app(app)
    app.init_app(migrate)
    app.run(port=5000, debug=True)