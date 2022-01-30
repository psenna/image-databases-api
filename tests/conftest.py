import os

import pytest_asyncio
DATABASE_URL = 'sqlite:///testedb.sqlite'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'True'

from typing import Generator
from fastapi.testclient import TestClient
import pytest
from app.app import app
from app.run_migration import run_migrations_test

@pytest_asyncio.fixture(scope="function")
def client() -> Generator:
    run_migrations_test()
    with TestClient(app) as c:
        yield c