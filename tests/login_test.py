import pytest
import os
from main import app, db
from apps.models.user import User
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__, template_folder='apps/templates',static_folder='apps/static')


db_uri = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER_USED')}:{os.getenv('MYSQL_ROOT_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["WTF_CSRF_ENABLED"] = False

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_register_user(client):
    response = client.post("/register", data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Registration successful" in response.data
    user = User.query.filter_by(email="test@example.com").first()
    assert user is not None

def test_register_existing_email(client):
    client.post("/register", data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }, follow_redirects=True)
    response = client.post("/register", data={
        "username": "anotheruser",
        "email": "test@example.com",
        "password": "password123"
    }, follow_redirects=True)
    assert b"Email already in use" in response.data

def test_login_invalid_credentials(client):
    response = client.post("/login", data={
        "email": "nonexistent@example.com",
        "password": "wrongpassword"
    }, follow_redirects=True)
    assert b"Invalid credentials" in response.data

def test_login_valid_credentials(client):
    client.post("/register", data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }, follow_redirects=True)
    response = client.post("/login", data={
        "email": "test@example.com",
        "password": "password123"
    }, follow_redirects=True)
    assert b"Login successful" in response.data

def test_logout(client):
    client.post("/register", data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }, follow_redirects=True)
    client.post("/login", data={
        "email": "test@example.com",
        "password": "password123"
    }, follow_redirects=True)
    response = client.get("/logout", follow_redirects=True)
    assert b"You have been logged out" in response.data
