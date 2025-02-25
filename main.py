from apps.app import app
from apps.config import *
from apps.models import *
import apps.routes.auth  

if __name__ == '__main__':
    app.run(port=5000, debug=True)