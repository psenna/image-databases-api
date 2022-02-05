import os
import pytest

import pytest_asyncio
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///dbteste.sqlite')
# DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/postgres'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'True'

from typing import Generator
from fastapi.testclient import TestClient
from tests.factories.user_factory import UserFactory
from app.app import app
from app.run_migration import run_migrations_test

@pytest.fixture
def client() -> Generator:
    with TestClient(app) as c:
        run_migrations_test()
        yield c

@pytest.fixture(scope="function")
async def super_user_token_header() -> Generator:
    yield await UserFactory.get_super_user_token_headers()

@pytest.fixture(scope="function")
async def regular_user_token_header() -> Generator:
    yield await UserFactory.get_regular_user_token_headers()