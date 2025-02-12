from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"

class SeverityLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class Status(Enum):
    SUCCESS = "success"
    ERROR = "error"