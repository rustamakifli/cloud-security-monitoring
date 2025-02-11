from app.config import db
from datetime import datetime
from app.models.constants import SeverityLevel

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cloud_provider = db.Column(db.String(10), nullable=False)  
    resource_id = db.Column(db.String(200), nullable=False) 
    issue_type = db.Column(db.String(255), nullable=False)  
    severity = db.Column(db.Enum(SeverityLevel), nullable=False) 
    description = db.Column(db.Text, nullable=False)  
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Alert {self.issue_type} - {self.resource_id}>"
