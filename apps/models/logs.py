from apps.config import db
from datetime import datetime
from apps.models.constants import Status

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(255), nullable=False)  
    status = db.Column(db.Enum(Status), nullable=False)
    details = db.Column(db.Text, nullable=True) 
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Log {self.action} - {self.status}>"
