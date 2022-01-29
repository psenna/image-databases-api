import os
DATABASE_URL = 'sqlite:///testedb.sqlite'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'true'

from typing import Generator
from fastapi.testclient import TestClient
import pytest
from app.app import app
from app.run_migration import run_migrations

@pytest.fixture(scope="function")
def client() -> Generator:
    run_migrations(DATABASE_URL)
    with TestClient(app) as c:
        yield c