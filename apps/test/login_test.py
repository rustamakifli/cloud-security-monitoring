import pytest
from apps.models import User
from apps.config import db
from main import app  


@pytest.fixture
def test_app():
    # Configure the app for testing
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # In-memory DB for tests
        "WTF_CSRF_ENABLED": False,  # Disable CSRF for testing forms
    })
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(test_app):
    return test_app.test_client()


def test_register_success(client):
    # Test registration with valid data
    response = client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "test@example.com",
            "password": "test1234",
            "confirm_password": "test1234",
        },
        follow_redirects=True,
    )
    assert b"Registration successful" in response.data
    # Ensure user was created in the database
    user = User.query.filter_by(email="test@example.com").first()
    assert user is not None
    assert user.username == "testuser"


def test_register_existing_email(client):
    # Register a user
    client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "test@example.com",
            "password": "test1234",
            "confirm_password": "test1234",
        },
        follow_redirects=True,
    )
    # Try to register with the same email again
    response = client.post(
        "/register",
        data={
            "username": "anotheruser",
            "email": "test@example.com",
            "password": "newpassword",
            "confirm_password": "newpassword",
        },
        follow_redirects=True,
    )
    assert b"Email already in use" in response.data


def test_login_invalid_credentials(client):
    # Register a user
    client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "test@example.com",
            "password": "test1234",
            "confirm_password": "test1234",
        },
        follow_redirects=True,
    )
    # Attempt to log in with an invalid password
    response = client.post(
        "/login",
        data={
            "email": "test@example.com",
            "password": "wrongpassword",
        },
        follow_redirects=True,
    )
    assert b"Invalid credentials" in response.data


def test_login_valid(client):
    # Register a user first
    client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "test@example.com",
            "password": "test1234",
            "confirm_password": "test1234",
        },
        follow_redirects=True,
    )
    # Now log in with correct credentials
    response = client.post(
        "/login",
        data={
            "email": "test@example.com",
            "password": "test1234",
        },
        follow_redirects=True,
    )
    assert b"Login successful" in response.data


def test_logout(client):
    # Register and log in a user first
    client.post(
        "/register",
        data={
            "username": "testuser",
            "email": "test@example.com",
            "password": "test1234",
            "confirm_password": "test1234",
        },
        follow_redirects=True,
    )
    client.post(
        "/login",
        data={
            "email": "test@example.com",
            "password": "test1234",
        },
        follow_redirects=True,
    )
    # Logout the user
    response = client.get("/logout", follow_redirects=True)
    assert b"You have been logged out" in response.data
