import pytest
import random
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app
from app.database import Base, get_db


import warnings
warnings.filterwarnings("ignore", message="The 'app' shortcut is deprecated")


SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    future=True
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(autouse=True)
def clean_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def test_user_with_tasks(client):
    username = f"testuser_{random.randint(1000, 9999)}"
    user_data = {
        "username": username,
        "first_name": "Test",
        "password": "testpass123"
    }
    client.post("/api/users/", json=user_data)
    
    login_res = client.post(
        "/api/token",
        data={"username": username, "password": "testpass123"}
    )
    token = login_res.json()["access_token"]
    
    tasks = [
        {"title": "Task 1", "status": "New"},
        {"title": "Task 2", "status": "In Progress"},
        {"title": "Task 3", "status": "Completed"}
    ]

    created_task_ids = []
    for task in tasks:
        res = client.post(
            "/api/tasks/",
            json=task,
            headers={"Authorization": f"Bearer {token}"}
        )
        created_task_ids.append(res.json()["id"])

    return {
        "username": username,
        "token": token,
        "task_ids": created_task_ids
    }
